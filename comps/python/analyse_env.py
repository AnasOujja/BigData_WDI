from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("Analyse Environment") \
    .getOrCreate()

# Lire le fichier CSV
df = spark.read.csv("/data/spark/files/WDI_environment.csv", header=True, inferSchema=True)

# Convertir le DataFrame Spark en DataFrame Pandas
pandas_df = df.toPandas()

# Exemple de visualisation avec Matplotlib
plt.figure(figsize=(10, 6))
plt.hist(pandas_df["CO2 emissions (kt)"].dropna(), bins=30, edgecolor='k')  # Utiliser dropna() pour enlever les valeurs nulles
plt.title("Distribution de CO2 emissions (kt)")
plt.xlabel("Valeurs de CO2 emissions (kt)")
plt.ylabel("Fréquence")
plt.grid(True)  # Ajouter une grille pour mieux visualiser
plt.savefig("/data/spark/files/figures/histogram.png")






















