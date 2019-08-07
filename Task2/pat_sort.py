import os
os.environ['PYSPARK_PYTHON']='/usr/local/bin/python3'
from pyspark import SparkContext
import findspark

sc = SparkContext( 'local', 'test')
logFile = "PAT.txt"
logData = sc.textFile(logFile,2).cache()

global basePara

basePara, fullScore = logData.collect()[0:2]
basePara = basePara.split(" ")
fullScore = fullScore.split(" ")

def sumAndFormat(x):
    baseScoreList = ["-" for i in range(int(basePara[1]))]
    sum = 0
    flag = 0
    questionList = x[1].split("#")
    scoreList = x[2].split("#")
    for index, quesNum in enumerate(questionList):
        if scoreList[index] == "-1":
            continue
        flag +=1
        baseScoreList[int(quesNum)-1] = scoreList[index]
        sum += int(scoreList[index])
    if sum>0:
        return [str(flag),x[0],str(sum)," ".join(baseScoreList)]

logData = logData.zipWithIndex().filter(lambda x:x[1]>1).map(lambda x:(" ".join(x[0].split(" ")[:2]),x[0].split(" ")))

logData = logData.reduceByKey(lambda x,y:x[2]>y[2] and x or y)

logData = logData.map(lambda x:(x[1][0],x[1])).sortByKey().reduceByKey(lambda x,y:[x[0],"#".join([x[1],y[1]]),"#".join([x[2],y[2]])])

logData = logData.map(lambda x:(x[0],sumAndFormat(x[1]))).filter(lambda x:x[1] is not None).sortBy(lambda x:x[1][1]).sortBy(lambda x:x[1][0]).sortBy(lambda x:x[1][2],ascending=False).zipWithIndex().map(lambda x:(x[1],x[0][1])).groupBy(lambda x:x[1][2]).sortBy(lambda x:x[0],ascending=False)

res = logData.collect()

sumScore = "#"
rank=-1
for index,paraList in enumerate(res):
    for para in paraList[1]:
        if sumScore == para[1][2]:
            print("{} {}".format(rank," ".join(para[1][1:])))       
        else:
            sumScore = para[1][2]
            rank = para[0]+1
            print("{} {}".format(rank," ".join(para[1][1:])))
    

