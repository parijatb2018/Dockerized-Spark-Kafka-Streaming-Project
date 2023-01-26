docker-compose -f spark-kafka.yml up -d

# docker-compose -f spark-kafka.yml up --scale spark-worker=3 -d

# docker-compose up --scale spark-worker=3