import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append('Level_2/datasets/')


import data_loader as loader
#import datasets
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR, SVC
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE

#from alipy.experiment.al_experiment import AlExperiment
from math import sqrt
import pickle
import warnings
warnings.filterwarnings("ignore")
import joblib
import time
# Seed = 0
# np.random.seed(Seed)

SAVE_MODEL=False
BENCHMARKS={"Pascal":loader.pascal_matrix_transcast(),"Sieve":loader.sieve_transcast(),"Meteor":loader.meteor_transcast(),"Scimark":loader.scimark_transcast(),"Raytrace":loader.raytraceParCast()}
for benchmark in BENCHMARKS:
    X, y, call_graph, dictionary = BENCHMARKS[benchmark]
    # X1, y1, c1, d1 = loader.scimarkParCast()

    # if y == y1:
        # print ("The same")
    # else:
        # print('Different')
        # print(X[1],loader.scimarkParCast()[0][1])


    CROSS_VALIDATION = 1
    int_to_str = {}
    for key in dictionary:
        int_to_str[dictionary[key]] = key
    #print(dictionary)
    node = []
    for x in X:
        temp = []
        for key in range(len(dictionary)):
            temp.append(x[int_to_str[key]])
        node.append(temp)
    X_node = np.array(node)

    print("==================================")
    y = np.array(y).reshape(-1, 1)
    y=y*100
    #MODEL = [LinearRegression(), MLPRegressor(), RandomForestRegressor(),
    #         DecisionTreeRegressor(), AdaBoostRegressor()]
    #MLPRegressor()
    MODEL=[LinearRegression()]

    '''for index in range(len(X_node)):
        print(y[index],X_node[index])'''

    def ratioSummary(true_arr, pred_arr, ratio = [.05, .1, .15,.25, 1]):
        pred_arr = pred_arr.reshape(-1, 1)
        abs_diff = np.abs(true_arr - pred_arr)
        abs_diff_ratio = np.divide(abs_diff, true_arr)
        count = []
        for rt in ratio:
            count.append(np.sum(abs_diff_ratio < rt))
        count[1] = count[1] - count[0]
        count[2] = count[2] - count[1] - count[0]
        count[3] = count[3] - count[2] - count[1] - count[0]
        count[4] = count[4] - count[3] - count[2] - count[1]-count[0]
        return count

    for train_size in [40]:
        for model in MODEL:
            Loss_RMSE, Loss_MAE, y_AVG = [], [], []
            print("Training size: ",train_size,"Testing size",len(y)-train_size)
            for cv in range(CROSS_VALIDATION):
                X_train, X_test, y_train, y_test = train_test_split(X_node, y, train_size=train_size)
                t1=time.time()
                model.fit(X_train, y_train)

                #print("--- %s seconds ---" % ((time.time() - t1)*1000))
                t3=time.time()
                y_pred = model.predict(X_test)
                error_ratio=np.abs(y_pred-y_test)/y_test
                t4=time.time()
                #print("--- %s seconds ---" % ((time.time() - t1)*1000))

                trian_times=[str(round(val[0],2)) for val in y_train]
                trian_times=", ".join(trian_times)
                #print(trian_times)
                error_ratio=error_ratio.flatten()
                error_ratio=np.multiply(error_ratio,100)
            
            
                rmse = sqrt(MSE(y_test, y_pred))
                mae = MAE(y_test, y_pred)
                #print(loss)
                Loss_RMSE.append(rmse)
                Loss_MAE.append(mae)
                y_AVG.append(y_test.mean())
                combined_array = np.column_stack((y_pred, y_test))
                #np.savetxt('pascal100_trans_output.txt', combined_array, fmt='%.8f %.8f')

            print(model)
            print(Loss_MAE)
            
            print('MSE (sec.): mean={:4f}; std={:4f}; var={:4f}'.format(np.array(Loss_RMSE).mean(), np.array(Loss_RMSE).std(),np.array(Loss_RMSE).var()))
            #print('MSE (ratio): {:4%}'.format(np.array(Loss_RMSE).mean() / np.array(y_AVG).mean()))
            print('MAE (sec.): mean={:4f}; std={:4f}; var={:4f}'.format(np.array(Loss_MAE).mean(), np.array(Loss_MAE).std(),np.array(Loss_MAE).var()))
            print('(Error ratio): {:4%}'.format(np.array(Loss_MAE).mean() / np.array(y_AVG).mean()))
            count = ratioSummary(y_test, y_pred)
            print('Error Count by Ratio :\n  <5%: {:d};\n  '
                '5%-10%: {:d};\n  10%-15%: {:d}; \n 15%-25%: {:d} \n  >25%: {:d}'.format(count[0], count[1], count[2], count[3],count[4]))
            print()
            print()
        if SAVE_MODEL:
            with open('models\modelchaos.pkl','wb') as f:
                pickle.dump(model,f)


