# hadoop-ecosystem-udemy
Hadoop tutorial with MapReduce, HDFS, Spark, Flink, Hive, HBase, MongoDB, Cassandra, Kafka + more! Over 25 technologies.

## set env
```sh
$ docker docker-deploy-hdp265.sh
...
# waiting for about 20min to downloaded it finish
...

# start docker
$ docker start sandbox-hdp
$ docker start sandbox-proxy

# stop docker
$ docker stop sandbox-hdp
$ docker stop sandbox-proxy

# insert to comfortable alias into shell
alias start-hdp="docker start sandbox-hdp && docker start sandbox-proxy"
alias stop-hdp="docker stop sandbox-hdp && docker stop sandbox-proxy"
alias hdp-term="docker exec -it sandbox-hdp /bin/sh; exit"
## TIP
# docker run을 할 때 local을 바인드 마운트 해놓기...
# reference: https://www.daleseo.com/docker-volumes-bind-mounts/
```