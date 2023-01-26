# docker rm -f $(docker ps -aq)

docker-compose -f spark-kafka.yml down

cd ~/bitnami/kafka

sudo rm -rf config/ data/

cd ~/scala/custom-docker-compose/checkpoint

sudo rm -rf *

sudo rm .*

cd ~/scala/custom-docker-compose/

sleep 2

