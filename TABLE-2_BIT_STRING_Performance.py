import numpy as np

import sys
import os
#sys.path.append('Level_2/datasets/')
 
# adding the parent directory to
# the sys.path.




from datasets import data_loader_bit_vector as loader
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR, SVC
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE
from math import sqrt
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("Table-2 Bit-String Performance")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
print("---------------------------------------------------------------------------")
for benchmark in ["Raytrace","Scimark",'Pascal','Sieve',"Nbody","Meteor","Chaos","Richard","Cpu"]:
    BENCHMARK=benchmark
    print(BENCHMARK)
    bit_dict,time_dict,cast_cost_dic=loader.loadthebBenchmark(BENCHMARK)

    X_node=[]
    y=[]
    for key in time_dict:
        X_node.append(np.fromstring(bit_dict[key], dtype=float, sep=','))
        y.append(float(time_dict[key]))

    X_node = np.array(X_node)
   

        
    y = np.array(y).reshape(-1, 1)
    
    CROSS_VALIDATION=1
    MODEL=[LinearRegression()]
    def ratioSummary(true_arr, pred_arr, ratio = [.05, .1, .15, 1]):
        pred_arr = pred_arr.reshape(-1, 1)
        abs_diff = np.abs(true_arr - pred_arr)
        abs_diff_ratio = np.divide(abs_diff, true_arr)
        count = []
        for rt in ratio:
            count.append(np.sum(abs_diff_ratio < rt))
        count[1] = count[1] - count[0]
        count[2] = count[2] - count[1] - count[0]
        count[3] = count[3] - count[2] - count[1] - count[0]
        return count
    for train_size in [40,.50]:
        for model in MODEL:
            Loss_RMSE, Loss_MAE, y_AVG = [], [], []
            
            for cv in range(CROSS_VALIDATION):
                X_train, X_test, y_train, y_test = train_test_split(X_node, y, train_size=train_size)
                print(len(X_train),len(y_train),len(X_test),len(y_test))
                model.fit(X_train, y_train)
                #print(len(y_train),len(y_test))
                y_pred = model.predict(X_test)
                error_ratio=np.abs(y_pred-y_test)/y_test
            
                error_ratio=error_ratio.flatten()
                error_ratio=np.multiply(error_ratio,100)
            
            
                rmse = sqrt(MSE(y_test, y_pred))
                mae = MAE(y_test, y_pred)
                #print(loss)
                Loss_RMSE.append(rmse)
                Loss_MAE.append(mae)
                y_AVG.append(y_test.mean())
           
            print(model)
            print(Loss_MAE)
            
            print('MSE (sec.): mean={:4f}; std={:4f}; var={:4f}'.format(np.array(Loss_RMSE).mean(), np.array(Loss_RMSE).std(),np.array(Loss_RMSE).var()))
            print('MSE (ratio): {:4%}'.format(np.array(Loss_RMSE).mean() / np.array(y_AVG).mean()))
            print('MAE (sec.): mean={:4f}; std={:4f}; var={:4f}'.format(np.array(Loss_MAE).mean(), np.array(Loss_MAE).std(),np.array(Loss_MAE).var()))
            print('MAE (ratio): {:4%}'.format(np.array(Loss_MAE).mean() / np.array(y_AVG).mean()))
            count = ratioSummary(y_test, y_pred)
            print('Error Count by Ratio :\n  <5%: {:d};\n  '
                '5%-10%: {:d};\n  10%-15%: {:d};\n  >15%: {:d}'.format(count[0], count[1], count[2], count[3]))
            print()
            print()
        
        '''f = open('raytrace_.txt', 'w')
        for val in res:
            f.write(str(val)+"\n")
        f.close()'''

