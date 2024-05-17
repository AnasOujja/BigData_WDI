#!/bin/bash
#
#

docker compose -f ~/projet/comps/hadoop/docker-compose.yml down -v
docker volume list | grep hadoop | awk '{ print $2 }' | xargs docker volume rm --force
