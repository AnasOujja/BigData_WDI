#!/bin/bash
#
#
# modification 2024 : test de la ram dispo et utilisation de tel ou tel fichier hadoop.env
#

if [ $(free --giga | grep "^Mem" | awk '{ print $2 }') -lt 8 ]
then cp hadoop-8goRAM.env hadoop.env
fi

docker network create hbase 2>/dev/null
docker compose -f ~/projet/comps/hadoop/docker-compose.yml up -d namenode
docker compose -f ~/projet/comps/hadoop/docker-compose.yml up -d datanode1 datanode2
docker compose -f ~/projet/comps/hadoop/docker-compose.yml up -d resourcemanager nodemanager1 nodemanager2 historyserver
docker compose -f ~/projet/comps/hadoop/docker-compose.yml up -d spark-master spark-worker-1 spark-worker-2

my_ip=`ip route get 1 | awk '{ for (i=1;i<=NF;i++) { if ( $i == "src" ) { print $(i+1) ; exit } } }'`
echo "Namenode: (HDFS Filebrowser) http://${my_ip}:9870"
echo "Spark-master: http://${my_ip}:28083"
echo "History Server: http://${my_ip}:28188"
