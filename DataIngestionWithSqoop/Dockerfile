FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Java & utilities
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    wget \
    curl \
    mysql-client \
    python3 \
    && apt-get clean

# Install Hadoop client
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz && \
    tar -xzf hadoop-3.2.1.tar.gz && \
    mv hadoop-3.2.1 /opt/hadoop

ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Sqoop
RUN wget https://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && \
    tar -xzf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz && \
    mv sqoop-1.4.7.bin__hadoop-2.6.0 /opt/sqoop

ENV SQOOP_HOME=/opt/sqoop
ENV PATH=$PATH:$SQOOP_HOME/bin

# MySQL JDBC Driver
RUN wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.49/mysql-connector-java-5.1.49.jar \
    -P $SQOOP_HOME/lib

CMD ["bash"]
