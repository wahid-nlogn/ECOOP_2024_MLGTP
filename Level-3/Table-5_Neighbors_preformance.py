import numpy as np
import pickle
import random
from numpy.core.defchararray import array
from numpy.core.fromnumeric import std
from numpy.lib.function_base import average
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append('Level_2/datasets/')

import data_loader_bit_vector as loader
from sklearn import metrics
import csv 
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE
from math import sqrt
import Common_Function as CF
import random
from collections import defaultdict

BENCHMARKS={"scimark":"Scimark","raytrace":"Raytrace","chaos":"Chaos","richard":"Richard","pascal":"Pascal","nbody":"Nbody","meteor":"Meteor","sieve":"Sieve","pdf":"Pdf",
            "benchfirst":"Benchfirst","cpu":"Cpu"}

BENCHMARK=BENCHMARKS["scimark"]
bit_dict,time_dict,cast_cost_dic,maxTyped_param,minTyped_param=CF.load_benchmark(BENCHMARK)

hashmap=defaultdict(list)
for key in bit_dict:
    temp=np.fromstring(bit_dict[key], dtype=int, sep=',')
    hashmap[np.sum(temp)].append(key)
def getCongifgs(source,k):
    arr=[]
    configs=[]
    for key in range(source,source+k,1):
        configs.extend(hashmap[key])
    arr=random.sample(configs, min(100,len(configs)))
    return arr
configs=getCongifgs(minTyped_param,5)
truecount=0
falsecount=0
diff=0
diff_ratios=0
for config in configs:
    for k in range(1,6,1):
        temp=CF.K_adjacentconfigurations(config,k,bit_dict)
        if len(temp)==0:
            continue
        predictted_neighbors=CF.predict_the_performance(BENCHMARK,temp)
        if len(predictted_neighbors)==0:
            continue
        predictted_neighbors.sort(key=lambda x:x[1])
        actual_neighbors=CF.original_Performance(BENCHMARK,temp,time_dict)
        actual_neighbors.sort(key=lambda x:x[1])
        trueFound=False
        p_neighbor=predictted_neighbors[-1][0]
        for index in range(len(predictted_neighbors)-1,len(predictted_neighbors)-1-3,-1):
            if actual_neighbors[-1][0]==predictted_neighbors[index][0]:
                truecount+=1
                trueFound=True
                p_neighbor=predictted_neighbors[index][0]
                break
        if not trueFound:
            falsecount+=1
        diff+=abs(actual_neighbors[-1][1]-time_dict[p_neighbor])
        diff_ratios+=(abs(actual_neighbors[-1][1]-time_dict[p_neighbor]))/actual_neighbors[-1][1]
print(BENCHMARK)
print("True/False Ratio",(truecount/(truecount+falsecount))*100,"True Count: ", truecount,"False Count: ", falsecount,"Total: ",truecount+falsecount)
print("averege difference: ", diff/(truecount+falsecount))
print("Difference Ratios: ",(diff_ratios/((truecount+falsecount)))*100,"%")

