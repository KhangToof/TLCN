from pyspark.sql import SparkSession

def connect_mongodb():
    spark = SparkSession.builder \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
    .config("spark.driver.maxResultSize", "6g") \
    .config("spark.driver.memory", "3g") \
    .config("spark.executor.memory", "3g") \
    .appName("yelp_dataset") \
    .getOrCreate()

    return spark