import csv

def create_conf(csv_file_path, conf_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)


        first = """\
input {
  stdin { }
}


filter {

csv {
  separator => ","
  columns =>

"""

        last = """\
output {
  stdout { codec => json }
  opensearch {
    hosts  => ["https://os01:9200","https://os02:9200","https://os03:9200"]
    auth_type => {
      type => 'basic'
      user => 'admin'
      password => 'admin'
    }
    cacert => "/usr/share/logstash/config/certificates/ca/ca.pem"
    ssl_certificate_verification => false
    template_name => "wdieconomy"
    template_overwrite => true
    template => "/data/opensearch/wdi_economy_template.json"
    index => "wdieconomy"
  }
}
"""

        # Writing header to the output text file
        with open(conf_file_path, 'w') as txt_file:
            txt_file.write(first)

            txt_file.write("[\n    ")
            txt_file.write(', '.join(['"' + column + '"' for column in header]))
            txt_file.write("\n  ]\n")
            txt_file.write("}\n")
            txt_file.write("}\n\n")

            txt_file.write(last)



csv_file_path = "../files/WDI_economy.csv" 
conf_file_path = "../opensearch/wdi_economy_conf.conf" 

create_conf(csv_file_path, conf_file_path)
