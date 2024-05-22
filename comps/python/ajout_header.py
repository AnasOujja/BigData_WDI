import pandas as pd

# Chemin vers le fichier source pour l'en-tête
source_header_file = "~/projet/comps/files/WDI_environment.csv"

# Chemin vers le fichier cible
target_file = "/home/anas/projet/comps/files/generated_files/fichier_without_header.csv"

# Lire le fichier source pour obtenir l'en-tête
header_df = pd.read_csv(source_header_file, nrows=0)

# Lire le fichier cible sans en-tête
target_df = pd.read_csv(target_file, header=None)

# Ajouter les en-têtes au DataFrame cible
target_df.columns = header_df.columns

# Écrire le DataFrame cible avec les nouveaux en-têtes dans un nouveau fichier
output_file = "/home/anas/projet/comps/files/generated_files/fichier_with_header.csv"
target_df.to_csv(output_file, index=False)

print(f"Le fichier avec l'en-tête ajouté a été enregistré sous {output_file}")

