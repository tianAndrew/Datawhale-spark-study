# Task 1:
## What have I met in Spark Installation.
* Different version of py
```
import os
os.environ['PYSPARK_PYTHON']='/usr/local/bin/pythonXXX' 
```
* Env variables
> Add sparkhome into path without bin because using bin/spark...
> `PATH=$SPARK_HOME:$PATH`

> Use pyspark
> `bin/pyspark`

## Expansion

1. Different between spark and mapreduce.
> There are 20 comparisons in this 
> [link](https://www.educba.com/mapreduce-vs-apache-spark/)
> And the most interesting part is spark's lineage.

2. RDD's essence
> They are basically datasets, which are distributed across a cluster (remember Spark framework is inherently based on an MPP architecture), and provide resilience (automatic failover) by nature.
> Here is a great [web](https://hub.packtpub.com/understanding-spark-rdd/) to learn about RDD easily. 
