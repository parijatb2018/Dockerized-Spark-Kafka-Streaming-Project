# Dockerized-Spark-Kafka-Streaming-Project

## Project Conceptualization and Targets
### Conceptualization:
This is a completely dockerized project where in every 10 seconds a new random name of a person is produced using a Python KAFKA producer and then it's fed to a KAFKA topic called 'rockthejvm' and then the topic is read by a PYSPARK-KAFKA consumer using Spark streaming[or microbatching] and an aggregation is done on the first alphabets of the names and for a one day window and then a count operation is done to find a list of alphabets and their counts. The aggregation result is subsequently fed and updated by the SPARK streaming to a KAFKA topic called 'stats'. 

The result is then consumed by a python-Kafka consumer and the results are written/updated on a mysql databse continiously.

At last a Flask App and d3.js library is used to read the data from mysql database and create a realtime beautiful barchart dashboard showing letters and their counts and also the changes in count dynamically in real time.

This project is conceptualized with a thought to be used in census or any type of statistical counting for a period and seeing the changes in realtime.

In this project stress has been put to make it as a highly reusable template project that can be used as a base and on top of that any customization or scaling can be done. The DevOps part consumes a lot of time initially in a project so it can be substantally reduced using such a template.
The containerized approach is taken to spin everything quickly and faster building and troubleshooting.

### Stack used[so far]
1. Spark3.3[bitnami image]
2. Kafka3.3[bitnami image]
3. zookeeper3.8[bitnami image]
4. Python3.8
5. Flask 2.0.2
6. Unbutu 20.4
7. MySql 8.0
8. d3.js v5 min
9. gunicorn 20.1.0

## Future targets
1. To scale the project to handle faster producer feed[multithreading]
2. Kafka scaling and better producer and consumer tuning
3. Using multi consumer to reduce lag
4. Better spark tuning to increase batching effeciency
5. Later discard the mysql db and Spark and make it a perfectly realtime one using Kafka-Streaming API
6. Using AIRFLOW to do some batch jobs
7. Include CICD 
8. Using Terraform when shifting the to AWS

## Image showing a static snap of the dashboard, producer, and stats topic consumer

<img width="1345" alt="Screen Shot 2023-02-04 at 8 34 45 PM" src="https://user-images.githubusercontent.com/43022026/216797259-a91f724d-4a7c-4911-b221-d220e6757ab3.png">

Top terminal> Producer
Middle terminal> stats topic consumer
D3.js real time dashbiard
#### Notice the lag in the result from producer to the dashboard

## The below GIF shows the realtime dashboard animation[a duration of 30s]

![Feb-04-2023 21-43-34](https://user-images.githubusercontent.com/43022026/216797340-11dcae82-c0e9-4725-85a1-579c1fd2c0df.gif)
