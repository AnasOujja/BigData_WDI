docker compose down
docker volume rm $(docker volume ls --filter "name=opensearch_os-data-*" -q)
