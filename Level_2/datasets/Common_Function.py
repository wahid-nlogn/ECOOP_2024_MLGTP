from unittest import result
import numpy as np
import pickle
from sklearn.metrics import mean_absolute_error as MAE
from numpy.core.fromnumeric import sort
import random
import data_loader_bit_vector as loader
def isMatches(nparray,indexes):
    for index in indexes:
        if nparray[index]==0:
            return False
    return True

def one_step_away(current_config_file_name,bit_dict):
    current_config_string=bit_dict[current_config_file_name]
    np_current_config=np.fromstring(current_config_string, dtype=int, sep=',')
    counttyped=np.sum(np_current_config==1)
    array_indexes=np.nonzero(np_current_config == 1)[0]
    res=[]
    
    for key,val in bit_dict.items():
        ndarray=np.fromstring(val, dtype=int, sep=',')
        if  isMatches(ndarray,array_indexes) and np.sum(ndarray==1)==counttyped+1:
            res.append(key)
        
    return res
def onestepAway(current_config_file_name,bit_dict,bit_string_to_file):
    current_config_string=bit_dict[current_config_file_name]
    arr1=current_config_string.split(',')
    result=[]
    for index,val in enumerate(arr1):
        if val=='0':
            result.append(index)
    files=[]
    for index in result:
        arr=bit_dict[current_config_file_name]
        arr=arr.split(',')
        arr[index]='1'
        newFile=",".join(arr)
        if newFile in bit_string_to_file:
            files.append(bit_string_to_file[newFile])
    return files

def K_adjacentconfigurations(current_config_file_name,k,bit_dict):
    #bit_dict,time_dict,cast_cost_dic=loadthebBenchmark(becnhmark)
    current_config_string=bit_dict[current_config_file_name]
    np_current_config=np.fromstring(current_config_string, dtype=int, sep=',')
    counttyped=np.sum(np_current_config==1)
    array_indexes=np.nonzero(np_current_config == 1)[0]
    res=[]
    cn=0
    for key,val in bit_dict.items():
        ndarray=np.fromstring(val, dtype=int, sep=',')
        if  isMatches(ndarray,array_indexes) and np.sum(ndarray==1)==counttyped+k:
            res.append(key)
            cn+=1
        if cn==20:
            break
    return res


def getStandardDev(benchmark,list_of_configuration):
    bit_dict,time_dict,cast_cost_dic=loader.loadthebBenchmark(benchmark)
    time=[]
    for config in list_of_configuration:
        time.append(float(time_dict[config]))
  
    return np.std(time)
def getDiffernceRatio(benchmark,list_of_configuration,model1=None):
    if not model1:
        model=load_model(benchmark)
    else:
        model=model1
    if len(list_of_configuration)==0:
        return (0,0)
    X,ys=processDataset(benchmark,list_of_configuration)
    y=[]
    for item in ys:
        y.append(item[0])
    
    '''print("In common function",len(X),len(y))
    print(len(X[0]),len(y[0]))
    print(X[0])'''
    #print(list_of_configuration)
    #for x in X:
    #    print(len(x),sep=" ",end=" ")
    y_predict=model.predict(X)
    y_predict=y_predict.flatten()
    #print(y_predict)
    #print(y)
    #std_dev=np.std(np.abs(y_predict-y))
  
    
    difference_ratio=((np.sum(np.abs(y_predict-y)/y))/len(y))*100
    std_dev=np.std((np.abs(y_predict-y)/y)*100)
    return difference_ratio,std_dev
def predict_the_performance(benchmark,list_of_configuration):
    model=load_model(benchmark)
    if len(list_of_configuration)==0:
        return np.array([])
    X,y=processDataset(benchmark,list_of_configuration)
    
    y_predict=model.predict(X)
    error_ratio=np.abs(y_predict-y)/y   
    error_ratio=error_ratio.flatten()
    error_ratio=np.sum(error_ratio)/len(y)
    error_ratio=np.multiply(error_ratio,100)
    #print(error_ratio)
    y_predict=np.array(y_predict).reshape(-1, 1)
    result=[]
    for j in range(len(y_predict)):
        result.append((list_of_configuration[j],y_predict[j]))
    
    return result
def predict_the_performance_with_model(benchmark,list_of_configuration,model):
    
    if len(list_of_configuration)==0:
        return np.array([])
    X,y=processDataset(benchmark,list_of_configuration)
    
    y_predict=model.predict(X)
    error_ratio=np.abs(y_predict-y)/y   
    error_ratio=error_ratio.flatten()
    error_ratio=np.sum(error_ratio)/len(y)
    error_ratio=np.multiply(error_ratio,100)
    #print(error_ratio)
    y_predict=np.array(y_predict).reshape(-1, 1)
    result=[]
    for j in range(len(y_predict)):
        result.append((list_of_configuration[j],y_predict[j]))
    
    return result
def original_Performance(benchmark,list_of_configurations,time_dict):
    if len(list_of_configurations)==0:
        return np.array([])
    
    original_time_list=[]
    for config_file in  list_of_configurations:
        original_time_list.append((config_file,time_dict[config_file]))
    
    return original_time_list
def getTotalTimeofthepath(benchmark,paths,time_dict):
    results=[]
    for path in paths:
        totaltime=0
        for config in path:
            totaltime+=time_dict[config]
        results.append((path,totaltime))
    #results.sort(key=lambda x:x[1])
    #results.sort(key=lambda x:x[1],reverse=True)
    random.shuffle(results)
    return results
def load_model(BENCHMARK):
    model=None
    if BENCHMARK=='Raytrace':
        with open('models\modelraytrace.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Scimark":
        with open('Level_2\datasets\models\modelscimark.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Sieve":
        with open('models\modelsieve.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK == "Nbody":
        with open('models\modelnbody.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK == "Pascal":
        with open('models\modelpascal.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK == "Meteor":
        with open('models\modelmeteor.pkl', 'rb') as f:
            model = pickle.load(f) 
    elif BENCHMARK=="Chaos":
        with open('models\modelchaos.pkl', 'rb') as f:
            model = pickle.load(f) 
    elif BENCHMARK=="Monte":
        with open('models\modelmonte.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Benchfirst":
        with open('models\modelbenchfirst.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Richard":
        with open('models\modelrichard.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Pdf":
        with open('models\modelzebrapdf.pkl', 'rb') as f:
            model = pickle.load(f)
    elif BENCHMARK=="Cpu":
        with open('models\modelcpu.pkl', 'rb') as f:
            model = pickle.load(f)
    
    return model
def processDataset(benchmark,current_config_files_name):
    if len(current_config_files_name)==0:
        return ([],[])
    bit_dict,time_dict,cast_cost_dic=loader.loadthebBenchmark(benchmark)
    lst_file_name_to_cast=[]
    lst_file_name_to_time=[]
    for file in current_config_files_name:
        lst_file_name_to_cast.append(file)
        lst_file_name_to_cast.append(cast_cost_dic[file])
        lst_file_name_to_time.append(file)
        lst_file_name_to_time.append(time_dict[file])
    X_onestep,y_onestep,call_graph,dictionary=[],[],{},{}
    import data_loader
    if benchmark in ["Raytrace","Monte","Chaos","Richard","Scimark","Pascal","Sieve","Benchfirst","Cpu"]:
        X_onestep, y_onestep, call_graph, dictionary=data_loader.retrunDatasetsNoCG(benchmark, lst_file_name_to_cast, lst_file_name_to_time)
        #print(dictionary)
    else:
        X_onestep, y_onestep, call_graph, dictionary=data_loader.retrunDatasets(benchmark, lst_file_name_to_cast, lst_file_name_to_time)
    
    
    '''print(X_onestep[0])
    print(y_onestep[0])
    print(dictionary)'''
    int_to_str = {}
    for key in dictionary:
        int_to_str[dictionary[key]] = key
    #print(int_to_str)
    node = []
    for x in X_onestep:
        temp = []
        for key in range(len(dictionary)):
            temp.append(x[int_to_str[key]])
            """if key in x:
                temp.append(x[int_to_str[key]])
            else:
                temp.append(0.0)"""
        node.append(temp)
    X_node_onestep = np.array(node)
    y_onestep = np.array(y_onestep).reshape(-1, 1)
    '''print(X_node_onestep[0])
    print(y_onestep[0])'''
    return X_node_onestep,y_onestep





# This function loads the data of bechmark and prints basic information about the bechmark
def load_benchmark(BENCHMARK):
    maxTyped_param=0
    minTyped_param=float('inf')
    maxTypeFile=""
    bit_dict,time_dict,cast_cost_dic=loader.loadthebBenchmark(BENCHMARK)
    print(BENCHMARK,len(time_dict),len(cast_cost_dic))
    
    filename=""
    for key in bit_dict:
        np_current_config=np.fromstring(bit_dict[key], dtype=int, sep=',')
        #maxTyped_param=max(maxTyped_param,np.sum(np_current_config))
        if np.sum(np_current_config)>maxTyped_param:
            maxTyped_param=np.sum(np_current_config)
            maxTypeFile=key
        minTyped_param=min(minTyped_param,np.sum(np_current_config))
        filename=key

    print("Max file name: ", maxTypeFile)

    return bit_dict,time_dict,cast_cost_dic,maxTyped_param,minTyped_param

def load_benchmark_transient(BENCHMARK):
    maxTyped_param=0
    minTyped_param=float('inf')
    
    bit_dict,time_dict,cast_cost_dic=loader.loadthebBenchmark_trainsient(BENCHMARK)
    print(BENCHMARK,len(time_dict),len(cast_cost_dic))
    
    filename=""
    for key in bit_dict:
        np_current_config=np.fromstring(bit_dict[key], dtype=int, sep=',')
        maxTyped_param=max(maxTyped_param,np.sum(np_current_config))
        minTyped_param=min(minTyped_param,np.sum(np_current_config))
        filename=key

    

    return bit_dict,time_dict,cast_cost_dic,maxTyped_param,minTyped_param