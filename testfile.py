
print('Hello From Spark')

import time

# Import SparkSession
from pyspark.sql import SparkSession

# from pyspark.sql import functions as F

from pyspark.sql.functions import *



# Create SparkSession 
spark = SparkSession.builder \
      .master("local[*]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 
      # .master("local[1]") \
      # .master("spark://spark-master:7077") \
      # .config("spark.driver.host", "localhost")
      

#sample dataframe to test some result

# data = [('James','','Smith','1991-04-01','M',3000),
#   ('Michael','Rose','','2000-05-19','M',4000),
#   ('Robert','','Williams','1978-09-05','M',4000),
#   ('Maria','Anne','Jones','1967-12-01','F',4000),
#   ('Jen','Mary','Brown','1980-02-17','F',-1)
# ]

# columns = ["firstname","middlename","lastname","dob","gender","salary"]
# df = spark.createDataFrame(data=data, schema = columns)

# df.show()


# df = spark.read.csv("/docker-app/pyspark-examples/resources/zipcodes.csv")
# df.printSchema()
# df.show()

#creating kafka connection and reading streaming DF

df_kafka = spark.readStream.format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("startingoffsets", "latest") \
  .option("failOnDataLoss","false") \
  .option("subscribe", "rockthejvm") \
  .load()

  # .option("kafka.bootstrap.servers", "localhost:9092") \
  # .option("kafka.bootstrap.servers", "172.18.0.4:9092") \
  #.option("kafka.bootstrap.servers", "http://kafka:9092") \
  # https://stackoverflow.com/questions/48797833/spark-structured-streaming-query-always-starts-with-auto-offset-rest-earliest-ev

#df_kafka.show()

df_kafka.printSchema()

time.sleep(5)

# Transformation part- aggregation

df_intermediate=df_kafka.withColumn('nameFirstLetter',substring(expr("cast(value as string) as value"),0,1))\
                 .select(col('nameFirstLetter'),col('timestamp').alias('eventTime'))\
                 .groupBy(window(col('eventTime'),'1 day').alias('timeWindow'),col('nameFirstLetter')) \
                 .agg(count('nameFirstLetter').alias('nameCountTotal'))\
                 .select(col('timeWindow').getField('start').alias('start'), \
                         col('timeWindow').getField('end').alias('end'),\
                         col('nameFirstLetter'),\
                         col('nameCountTotal')) #\
                #  .orderBy(col('nameFirstLetter'))
                 #.orderBy(col('nameCountTotal').desc())

# Printing in console 

# df_intermediate \
# .writeStream \
# .format("console") \
# .outputMode("complete") \
# .start() \
# .awaitTermination()


# writing to another kafka topic stats

df_stats=df_intermediate.select(col('nameFirstLetter').alias('key'),expr('cast(nameCountTotal as string) as value'))


df_stats\
  .writeStream \
  .format('kafka')\
  .option('kafka.bootstrap.servers', 'kafka:9092') \
  .option('topic', 'stats') \
  .option('checkpointLocation','checkpoint')\
  .outputMode("update")\
  .start()\
  .awaitTermination()