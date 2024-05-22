from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import pandas as pd
import matplotlib.pyplot as plt

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("Visualisation WDI avec PySpark") \
    .getOrCreate()

# Lire le fichier CSV
df = spark.read.csv("hdfs://tmp/data/WDI_environment.csv", header=True, inferSchema=True)

# Filtrer les données selon les critères spécifiés
df_filtered = df.filter(
    (col("renewable energy consumption (% of total final energy consumption)").between(30, 100)) &
    (col("forest area (% of land area)").between(40, 100))
)

# Agréger les données par pays et calculer la moyenne de la consommation d'énergie renouvelable et de la superficie forestière
df_grouped = df_filtered.groupBy("Country Name").agg(
    avg("renewable energy consumption (% of total final energy consumption)").alias("avg_renewable_energy"),
    avg("forest area (% of land area)").alias("avg_forest_area")
)

# Convertir le DataFrame Spark en DataFrame Pandas pour la visualisation
pandas_df = df_grouped.toPandas()

# Limiter 10 pays. Vous pouvez choisir vos propres pays ou les 10 premiers dans le DataFrame
selected_countries = pandas_df["Country Name"].unique()[:10]
pandas_df = pandas_df[pandas_df["Country Name"].isin(selected_countries)]

# Créer la visualisation avec Matplotlib
plt.figure(figsize=(12, 8))
for country in pandas_df["Country Name"].unique():
    country_data = pandas_df[pandas_df["Country Name"] == country]
    plt.plot(country_data["avg_forest_area"], country_data["avg_renewable_energy"], marker='o', linestyle='-', label=country)

plt.title("Visualisation de la consommation d'énergie renouvelable et de la superficie forestière")
plt.xlabel("Superficie forestière moyenne (% de la superficie totale des terres)")
plt.ylabel("Consommation d'énergie renouvelable moyenne (% de la consommation énergétique totale finale)")
plt.legend(title="Pays", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Enregistrer la figure
output_dir = "/data/spark/files/figures/"
output_path = f"{output_dir}/renewable_energy_forest_area_visualization_limited.png"
plt.savefig(output_path)
plt.show()

# Arrêter la session Spark
spark.stop()

