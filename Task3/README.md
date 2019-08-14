# Task 3
## Spark SQL

[Spark SQL](http://dblab.xmu.edu.cn/blog/1717-2/)

## Differences between RDD and DataFrame

[Differences between RDD and DataFrame](http://dblab.xmu.edu.cn/blog/1718-2/)

## Create DataFrame

* [Create DataFrame](http://dblab.xmu.edu.cn/blog/1719-2/)

'''
spark=SparkSession.builder.getOrCreate()
df = spark.read.json("file:///Users/andrew/DataWhale/Datawhale-spark-study/Task3/people.json")

df.show()
+----+-------+
| age|   name|
+----+-------+
|null|Michael|
|  30|   Andy|
|  19| Justin|
+----+-------+

df.printSchema()
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)

df.select(df.name,df.age + 1).show()
+-------+---------+
|   name|(age + 1)|
+-------+---------+
|Michael|     null|
|   Andy|       31|
| Justin|       20|
+-------+---------+

df.filter(df.age>22 ).show()
+---+----+
|age|name|
+---+----+
| 30|Andy|
+---+----+

df.groupBy("age").count().show()
+----+-----+
| age|count|
+----+-----+
|  19|    1|
|null|    1|
|  30|    1|
+----+-----+

df.sort(df.age.desc()).show()
+----+-------+
| age|   name|
+----+-------+
|  30|   Andy|
|  19| Justin|
|null|Michael|
+----+-------+

df.sort(df.age.desc(), df.name.asc()).show()
+----+-------+
| age|   name|
+----+-------+
|  30|   Andy|
|  19| Justin|
|null|Michael|
+----+-------+

df.select(df.name.alias("username"),df.age).show()
+--------+----+
|username| age|
+--------+----+
| Michael|null|
|    Andy|  30|
|  Justin|  19|
+--------+----+
'''

### [Connect DataFrame by JDBC](http://dblab.xmu.edu.cn/blog/1724-2/)

### [Stream Computing](http://dblab.xmu.edu.cn/blog/1732-2/)

### [Spark Streaming](http://dblab.xmu.edu.cn/blog/1733-2/)

### [DStream Operation](http://dblab.xmu.edu.cn/blog/1737-2/) 
