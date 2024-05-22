from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("Calcul des valeurs nulles dans le dataset WDI") \
    .getOrCreate()

# Lire le fichier CSV depuis HDFS
df = spark.read.csv("hdfs://namenode:9000/tmp/data/WDI_environment.csv", header=True, inferSchema=True)

# Afficher le schéma du DataFrame pour comprendre la structure des données
df.printSchema()

# Sélectionner les colonnes nécessaires
columns = df.columns

# Calculer le nombre de valeurs nulles pour chaque pays et pour chaque indicateur
null_counts = df.groupBy("Country Name").agg(
    *[spark_sum(col(c).isNull().cast("int")).alias(f"{c}_null_count") for c in columns if c != "Country Name"]
)

# Afficher les résultats
null_counts.show()

# Convertir le résultat en Pandas DataFrame pour un affichage plus convivial (optionnel)
pandas_null_counts = null_counts.toPandas()
print(pandas_null_counts)

# Ecrire les résultats en partitions dans HDFS
output_dir_hdfs = "hdfs://namenode:9000/tmp/data/null_counts_by_country"
null_counts.write.mode("overwrite").option("header", "false").csv(output_dir_hdfs)

# Arrêter la session Spark
spark.stop()
