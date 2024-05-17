import csv

def create_template(csv_file_path, txt_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        
        # Writing header to the output text file
        with open(txt_file_path, 'w') as txt_file:
            txt_file.write('{"index_patterns": ["wdienvironment*"],\n "settings": {\n"index": {\n"number_of_shards": 1,\n"number_of_replicas": 1,\n"refresh_interval": "5s"\n}\n},\n"mappings": {\n"properties": {\n')
            for i, column in enumerate(header):
                if column in ["Country Name"]:
                    txt_file.write(f'  "{column}": {{\n')
                    txt_file.write('    "type": "keyword"\n')
                    txt_file.write('  },\n')
                elif column == "Year":
                    txt_file.write(f'  "{column}": {{\n')
                    txt_file.write('    "type": "date",\n')
                    txt_file.write('    "format": "yyyy"\n')
                    txt_file.write('  },\n')
                else:
                    txt_file.write(f'  "{column}": {{\n')
                    txt_file.write('    "type": "float"\n')
                    if i == len(header) - 1:
                        txt_file.write('  }\n')
                    else:
                        txt_file.write('  },\n')
            txt_file.write("}\n")
            txt_file.write("}\n")
            txt_file.write("}")


create_template('../files/WDI_environment.csv', '../opensearch/wdi_environment_template.json')

