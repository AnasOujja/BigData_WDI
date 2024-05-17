echo "ATTENTION êtes vous bien sûr de lancer opensearch pour la première fois"
echo "CTRL-C pour arrêter - RETURN pour continuer"
read
sudo sysctl -w vm.max_map_count=512000
sudo /bin/rm -rf certs
bash generate-certs.sh
docker compose up -d
echo "Hey, patience is the key...Anas"
sleep 90
echo "activation de la sécurité"
docker compose exec os01 bash -c "chmod +x plugins/opensearch-security/tools/securityadmin.sh && bash plugins/opensearch-security/tools/securityadmin.sh -cd config/opensearch-security -icl -nhnv -cacert config/certificates/ca/ca.pem -cert config/certificates/ca/admin.pem -key config/certificates/ca/admin.key -h localhost"
