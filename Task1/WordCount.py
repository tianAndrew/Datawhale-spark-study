import os
os.environ['PYSPARK_PYTHON']='/usr/local/bin/python3' 
from pyspark import SparkContext
import findspark

sc = SparkContext( 'local', 'test')
logFile = "../Installation/README.md"
logData = sc.textFile(logFile, 2).cache()
numAs = logData.filter(lambda line: 'Step' in line).count()
numBs = logData.filter(lambda line: 'install' in line).count()
print('Lines with a: %s, Lines with b: %s' % (numAs, numBs))
