import numpy as np
from numpy.core.records import array
import csv 
import matplotlib.pyplot as plt
import sys
#sys.path.append('Level_2/datasets/')
import re, seaborn as sns
from datasets import data_loader as loader
from sklearn.cluster import KMeans
import pickle
from matplotlib.pyplot import figure





plt.rcParams.update({'font.size': 13})
#Set desired benchmark
BENCHMARK="Raytrace"
def load_model():
    model=None
    if BENCHMARK=='Raytrace':
        with open('modelraytrace.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Scimark":
        with open('modelscimark.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Sieve":
        with open('modelsieve.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK == "Nbody":
        with open('modelnbody.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=='Pascal':
        with open('modelpascal.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=='Meteor':
        with open('modelmeteor.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=='Monte':
        with open('modelmonte.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=='Chaos':
        with open('modelchaos.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=='Richard':
        with open('modelrichard.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=="Pdf":
        with open('modelzebrapdf.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=="Benchfirst":
        with open('modelbenchfirst.pkl','rb') as f:
            model=pickle.load(f)
    elif BENCHMARK=="Cpu":
        with open('modelcpu.pkl','rb') as f:
            model=pickle.load(f)
    return model
def find_clusters(y):
    kmeans = KMeans(n_clusters=4, random_state=0).fit(y)
    cluster_centers=kmeans.cluster_centers_
    #print(cluster_centers)
    arr=[]
    for val in cluster_centers:
        arr.append(val[0])
    arr.sort()
    return arr
def categorical_(X,Y,arr):
    new_X= [[],[],[],[],[]]
    new_y=[[],[],[],[],[]]
    for x,y in zip(X,Y):
        if y<=arr[0]:
            new_X[0].append(x)
            new_y[0].append(y)
        elif arr[0]<y<=arr[1]:
            new_X[1].append(x)
            new_y[1].append(y)
        elif arr[1]<y<=arr[2]:
            new_X[2].append(x)
            new_y[2].append(y)
        elif arr[2]<y<=arr[3]:
            new_X[3].append(x)
            new_y[3].append(y)
        elif y>arr[3]:
            new_X[4].append(x)
            new_y[4].append(y)
    
    return (new_X,new_y)
def draw_plot():
    X,y=loader.load_data_Sets_X_Y_dictionary(BENCHMARK)
    
    model=load_model()
    arr=find_clusters(y)
    
    cn1,cn2,cn3,cn4,cn5=0,0,0,0,0
    cn1=len(list(filter(lambda x:x<=arr[0],y)))
    cn2=len(list(filter(lambda x: arr[0]<x<=arr[1],y)))
    cn3=len(list(filter(lambda x: arr[1]<x<=arr[2],y)))
    cn4=len(list(filter(lambda x: arr[2]<x<=arr[3],y)))
    cn5=len(list(filter(lambda x: x>arr[3],y)))
    #figure(figsize=(8, 8), dpi=80)
    #print(cn1,cn2,cn3,cn4,cn5)
    myarray_x,myarray_y=categorical_(X,y,arr)
    x1,y1=myarray_x[0],myarray_y[0]
    x2,y2=myarray_x[1],myarray_y[1]
    x3,y3=myarray_x[2],myarray_y[2]
    x4,y4=myarray_x[3],myarray_y[3]
    x5,y5=myarray_x[4],myarray_y[4]
    #print(len(x1),len(x2),len(x3),len(x4),len(x5))
    #print(len(y1),len(y2),len(y3),len(y4),len(y5))

    y1_pred=model.predict(x1) if len(x1)>0 else [0]
    y2_pred=model.predict(x2) if len(x2)>0 else [0]
    y3_pred=model.predict(x3) if len(x3)>0 else [0]
    y4_pred=model.predict(x4) if len(x4)>0 else [0]
    y5_pred=model.predict(x5) if len(x5)>0 else [0]
   

    error_ratio_1=np.abs(y1_pred-y1)/y1 if len(y1)>0 else [0]
    error_ratio_2=np.abs(y2_pred-y2)/y2 if len(y2)>0 else [0]
    error_ratio_3=np.abs(y3_pred-y3)/y3 if len(y3)>0 else [0]
    error_ratio_4=np.abs(y4_pred-y4)/y4 if len(y4)>0 else [0]
    error_ratio_5=np.abs(y5_pred-y5)/y5 if len(y5)>0 else [0]
    
    green=findGreen([error_ratio_1,error_ratio_2,error_ratio_3,error_ratio_4,error_ratio_5])
    cyan=findCyan([error_ratio_1,error_ratio_2,error_ratio_3,error_ratio_4,error_ratio_5])
    blue=findBlue([error_ratio_1,error_ratio_2,error_ratio_3,error_ratio_4,error_ratio_5])
    purple=findPurple([error_ratio_1,error_ratio_2,error_ratio_3,error_ratio_4,error_ratio_5])
    red=findRed([error_ratio_1,error_ratio_2,error_ratio_3,error_ratio_4,error_ratio_5])
    #print(green,cyan,blue,purple,red)
    """green=[108,543,598,543,706]
    cyan=[20,25,18,17,17]
    blue=[25,10,7,5,2]
    purple=[8,3,2,1,10]
    red=[5,1,1,2,10]
    print(green,cyan,blue,purple,red)"""
    totals = [i+j+k+l+m for i,j,k,l,m in zip(green, cyan, blue,purple,red)]

    zero_to_five=[i / j * 100 for i,j in zip(green, totals)]
    five_to_ten= [i / j * 100 for i,j in zip(cyan, totals)]
    ten_to_fifteen=[i / j * 100 for i,j in zip(blue, totals)]
    fifteen_to_twenty=[i / j * 100 for i,j in zip(purple, totals)]
    twenty_to_above=[i / j * 100 for i,j in zip(red, totals)]

    
    bars1 = np.add(five_to_ten, zero_to_five).tolist()
    bars2 = np.add(bars1, ten_to_fifteen).tolist()
    bars3 = np.add(bars2, fifteen_to_twenty).tolist()
    r = [0,1,2,3,4]
 
    # Names of group and bar width
    names = ['0-'+str(arr[0])[:4],str(arr[0])[:4]+"-"+str(arr[1])[:4],str(arr[1])[:4]+"-"+str(arr[2])[:4],str(arr[2])[:4]+"-"+str(arr[3])[:4],">"+str(arr[3])[:4]+"s"]
    barWidth = .85
    plt.bar(r,zero_to_five, color='g', edgecolor='white', width=barWidth,tick_label="x",label="0%-5%")
    
    # Create green bars (middle), on top of the first ones
    plt.bar(r, five_to_ten, bottom=zero_to_five, color='c', edgecolor='white', width=barWidth,label="5%-10%")
    # Create green bars (top)
    plt.bar(r, ten_to_fifteen, bottom=bars1, color='blue', edgecolor='white', width=barWidth,label="10%-15%")
    
    plt.bar(r, fifteen_to_twenty, bottom=bars2, color='purple', edgecolor='white', width=barWidth,label="15%-20%")
    
    plt.bar(r, twenty_to_above, bottom=bars3, color='g', edgecolor='white', width=barWidth,label=">20%")
    # Custom X axis
    
    #plt.legend(loc="upper right")
    plt.title("CPU",fontsize=15)
    #plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
    #names=["0-33","33-80.3","80.3-86.9","86.9-101.5",">101.5"]
    plt.xticks(r, names)
    #plt.xlabel("Time(seconds) range",fontsize=15)
    plt.ylabel("% of configurations",fontsize=15)
    # Show graphic
    plt.ylim(top = 100)
    """path=r'Paper_ECOOP2024\BAR_CHART' + '\\'+BENCHMARK+".png"
    plt.savefig(path, 
               bbox_inches='tight', 
               transparent=True,
               pad_inches=0)"""
    #plt.show()
    path=r'figure8' + '\\'+BENCHMARK+".png"
    plt.savefig(path, 
               bbox_inches='tight', 
               transparent=True,
               pad_inches=0)
    #plt.savefig(os.path.join("figure7", filename))
    #plt.show()
def findGreen(error_ratios):
    res=[]
    for error_ratio in error_ratios:
        cn=0
        for val in error_ratio:
            #print(val)
            if val[0]<=0.05:
                cn+=1
        res.append(cn)
    return res
def findCyan(error_ratios):
    res=[]
    for error_ratio in error_ratios:
        cn=0
        for val in error_ratio:
            if 0.05<val[0]<=0.1:
                cn+=1
        res.append(cn)
    return res
def findBlue(error_ratios):
    res=[]
    for error_ratio in error_ratios:
        cn=0
        for val in error_ratio:
            if 0.1<val[0]<=0.15:
                cn+=1
        res.append(cn)
    return res
def findPurple(error_ratios):
    res=[]
    for error_ratio in error_ratios:
        cn=0
        for val in error_ratio:
            if 0.15<val[0]<=0.20:
                cn+=1
        res.append(cn)
    return res
def findRed(error_ratios):
    res=[]
    for error_ratio in error_ratios:
        cn=0
        for val in error_ratio:
            if val[0]>0.20:
                cn+=1
        res.append(cn)
    return res
draw_plot()