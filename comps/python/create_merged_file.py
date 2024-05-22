import subprocess
import os

# Définir les chemins
output_dir_hdfs = "hdfs://namenode:9000/tmp/data/null_counts_by_country"
namenode_partition_dir = "/tmp/data/generated_files/partitions"
local_output_path = "~/projet/comps/files/null_counts_by_country.csv"
local_partition_dir = "~/projet/comps/files/generated_files/partitions"

#local_output_path = "/tmp/null_counts_by_country.csv"
#hdfs_merged_output_path = "hdfs://namenode:9000/tmp/data/null_counts_by_country_merged.csv"
#local_final_path = "/tmp/data/generated_files/null_counts_by_country_merged.csv"

# Télécharger les partitions localement pour traitement
subprocess.run(f"docker exec -it namenode hfs dfs -get {output_dir_hdfs} {namenode_partition_dir}", shell=True)
# Fusionner les partitions en un seul fichier en supprimant les en-têtes redondants
with open(local_output_path, 'w') as outfile:
    for i, filename in enumerate(sorted(os.listdir(local_partition_dir))):
        if filename.endswith(".csv"):
            with open(os.path.join(local_partition_dir, filename), 'r') as infile:
                # Ecrire les en-têtes seulement pour le premier fichier
                if i == 0:
                    outfile.write(infile.readline())  # Ecrire les en-têtes
                else:
                    infile.readline()  # Ignorer les en-têtes
                # Copier le reste du fichier
                outfile.write(infile.read())

# Copier le fichier fusionné de local vers HDFS
#subprocess.run(f"hdfs dfs -put {local_output_path} {hdfs_merged_output_path}", shell=True)

# Récupérer le fichier fusionné sur le système local
# subprocess.run(f"hdfs dfs -get {hdfs_merged_output_path} {local_final_path}", shell=True)

