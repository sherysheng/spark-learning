import pyspark
import os
import sys

if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/srv/spark'

    # Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

print SPARK_HOME
print ""