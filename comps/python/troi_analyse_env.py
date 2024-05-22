from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum
from pyspark.sql.types import StructType, StructField, StringType
#import os

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Calcul des valeurs nulles dans le dataset WDI") \
    .getOrCreate()

# Read the CSV file from HDFS
df = spark.read.csv("hdfs://namenode:9000/tmp/data/WDI_environment.csv", header=True, inferSchema=True)

# Display the schema of the DataFrame to understand the data structure
df.printSchema()

# Select the necessary columns
columns = df.columns

# Calculate the number of null values for each country and for each indicator
null_counts = df.groupBy("Country Name").agg(
    *[spark_sum(col(c).isNull().cast("int")).alias(f"{c}_null_count") for c in columns if c != "Country Name"]
)

# Display the results
null_counts.show()

# Convert the result to a Pandas DataFrame for a more friendly display (optional)
pandas_null_counts = null_counts.toPandas()
print(pandas_null_counts)

# Write the results in partitions to HDFS
output_dir_hdfs = "hdfs://namenode:9000/tmp/data/null_counts_by_country"
null_counts.write.mode("overwrite").option("header", "false").csv(output_dir_hdfs)

# Extract the header from the original DataFrame and save it to a separate file
header_columns = ["Country Name"] + [f"{c}_null_count" for c in columns if c != "Country Name"]

# Create an empty Spark DataFrame with the header columns
schema = StructType([StructField(col_name, StringType(), True) for col_name in header_columns])
header_df = spark.createDataFrame([], schema)

# Define the path for the header CSV file
header_csv_path = "hdfs://namenode:9000/tmp/data/null_counts_by_country"

# Write the header DataFrame to HDFS
header_df.write.mode("append").option("header", "true").csv(header_csv_path)

#header_df.write.mode("overwrite").option("header", "true").csv(header_csv_path)

# Stop the Spark session
spark.stop()
