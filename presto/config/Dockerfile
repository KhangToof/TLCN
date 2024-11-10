FROM prestodb/presto:latest

USER root

VOLUME ./presto/config:/usr/lib/presto/etc

RUN mkdir -p /etc/catalog 

ADD delta.properties /opt/presto-server/etc/catalog/
ADD hive.properties /opt/presto-server/etc/catalog/

ENV PRESTO_JVM_CONFIG='/usr/lib/presto/etc/jvm.config'
ENV PRESTO_CONFIG_PROPERTIES='/usr/lib/presto/etc/config.properties'

