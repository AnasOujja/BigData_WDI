load () {
    FILE=/data/opensearch/files/WDI_environment.csv
    curl -XDELETE https://os01:9200/wdienvironment?pretty -u 'admin:admin' -k
    cat $FILE | /usr/share/logstash/bin/logstash -f /data/opensearch/wdi_environment_conf.conf --path.data /tmp

    FILE=/data/opensearch/files/WDI_economy.csv
    curl -XDELETE https://os01:9200/wdieconomy?pretty -u 'admin:admin' -k
    cat $FILE | /usr/share/logstash/bin/logstash -f /data/opensearch/wdi_economy_conf.conf --path.data /tmp
}

load
