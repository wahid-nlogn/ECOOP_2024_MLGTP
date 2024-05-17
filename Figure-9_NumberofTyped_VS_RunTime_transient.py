

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

from datasets import Common_Function as CF
import random
from datasets import data_loader_bit_vector as loader

print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("Figure-9")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")

BENCHMARKS={"scimark":"Scimark","raytrace":"Raytrace","richard":"Richard","pascal":"Pascal","meteor":"Meteor","sieve":"Sieve"}

#Change to your desire bechmark
for benchmark in BENCHMARKS:
    BENCHMARK=BENCHMARKS[benchmark]


    bit_dict,time_dict,cast_cost_dic,maxTyped_param,minTyped_param=CF.load_benchmark_transient(BENCHMARK)
    print(BENCHMARK,"Max typed: ",maxTyped_param,"Min Typed: ",minTyped_param)
    XS,YS=[],[]
    for key in bit_dict:
        array=np.fromstring(bit_dict[key],sep=",")
        temp_sm=np.count_nonzero(array == 1)
    
        YS.append(float(time_dict[key]))
        XS.append(temp_sm)
    x = np.array(XS)
    #random_array = np.random.choice([0, 1], size=x.shape)
    y = np.array(YS)

    N = len(XS)

    colors = np.random.rand(N)
    area = (40 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.title(BENCHMARK, fontsize=16)
    filename=BENCHMARK+".png"
    plt.xlabel("Number of parameters typed", fontsize=16)
    plt.ylabel("Run time(sec)", fontsize=16)
    plt.scatter(x, y)
    plt.savefig(os.path.join("figure9", filename))

