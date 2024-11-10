FROM bitnami/spark:3.4

USER root

RUN apt-get update && apt-get install curl -y

# curl some dependencies for spark
RUN curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
    && curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar \
    && curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.262/aws-java-sdk-1.12.262.jar \
    && curl -O https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar \
    && curl -O https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar \
    && curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.262/aws-java-sdk-s3-1.12.262.jar \
    && mv *.jar /opt/bitnami/spark/jars/

ENV SPARK_MODE='master'
ENV SPARK_MASTER_URL='spark://172.30.192.1:7077'
ENV SPARK_RPC_AUTHENTICATION_ENABLED='no'
ENV SPARK_RPC_ENCRYPTION_ENABLED='no'
ENV SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED='no'
ENV SPARK_SSL_ENABLED='no'
ENV SPARK_DRIVER_MEMORY='2g' 
ENV SPARK_DRIVER_CORES='2' 
