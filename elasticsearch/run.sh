#!/bin/bash


docker run -v $PWD/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -p 9200:9200 -d --name es_5 elasticsearch:5.2.2

docker run -p 9100:9100 -d mobz/elasticsearch-head:5