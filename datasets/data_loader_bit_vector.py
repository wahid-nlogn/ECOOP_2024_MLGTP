#import pandas as pd
import numpy as np
import os
import ast
PATH = os.getcwd()

#from ..Level_2/datasets.data_loader import nbody, scimarkParCast, sieve

#PATH="../"
def processData(benchmarkName,linesFile1,linesFile2,linesFile3):
    bit_dict, time_dict,cast_cost_dic = {}, {}, {}
    x_filename = ""
    y_filename = ""
    for i in range(len(linesFile1)):
        if i % 2 == 0:
            x_filename = linesFile1[i]
            x_filename=x_filename.strip()
        else:
            data = linesFile1[i]
            #string=linesFile2[i].split(' ')
            #y_arr[y_filename] = float(string[-1])
            #bit_dict[x_filename] = np.fromstring(data, dtype=int, sep=',')
            bit_dict[x_filename]=data
    for i in range(len(linesFile2)):
        if i % 2 == 0:
            y_filename = linesFile2[i]
            y_filename=y_filename.strip()
        else:
            #string=linesFile2[i].split(' ')
            string=linesFile2[i].split(' ')
            time_dict[y_filename] = float(string[-1])
            
            
            #time_dict[y_filename] = float(linesFile2[i])

    for i in range(len(linesFile3)):
        if i % 2 == 0:
            x_filename = linesFile3[i]
            x_filename=x_filename.strip()
        else:
            data = linesFile3[i]
            cast_cost_dic[x_filename] = data
    #print(time_dict)
    return bit_dict,time_dict,cast_cost_dic
def pascal(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "pascal_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "pascal_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "pascal_fc_nli_argcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("pascal",linesFile1,linesFile2,linesFile3)

def trans_pascal(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "pascal_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_pascal.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "pascal_fc_nli_argcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("pascal",linesFile1,linesFile2,linesFile3)
def raytrace():
    file1 = open(os.path.join(PATH, "datasets", "raytrace_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "raytrace_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "raytrace_fc_nli_parcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Raytrace",linesFile1,linesFile2,linesFile3)
def raytrace_trans():
    file1 = open(os.path.join(PATH, "datasets", "raytrace_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_raytrace.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "raytrace_fc_nli_parcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Raytrace",linesFile1,linesFile2,linesFile3)

def sieve_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "sieve_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "sieve_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "sieve_fc_nli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Raytrace",linesFile1,linesFile2,linesFile3)

def sieve_trans_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "sieve_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_sieve.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "sieve_fc_nli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Sieve",linesFile1,linesFile2,linesFile3)

def meteor_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "meteor_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "meteor_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "meteor_fc_nonli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Meteor",linesFile1,linesFile2,linesFile3)

def meteor_trans_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "meteor_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_meteor.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "meteor_fc_nonli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Meteor",linesFile1,linesFile2,linesFile3)


def nbody_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "bit_strings_nbody.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "nbody_log_thinkpadp17.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "nbody_fc_nli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Nbody",linesFile1,linesFile2,linesFile3)
def nbody_trans_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "bit_strings_nbody.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "nbody_log_thinkpadp17.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "nbody_fc_nli.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Nbody",linesFile1,linesFile2,linesFile3)

def scimark():
    file1 = open(os.path.join(PATH, "datasets", "scimark_bit_strings.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "SOR_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "SOR_fc_nli_parcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Scimark",linesFile1,linesFile2,linesFile3)
def scimark_trans():
    file1 = open(os.path.join(PATH, "datasets", "scimark_bit_strings.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_SOR.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "SOR_fc_nli_parcast.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Scimark",linesFile1,linesFile2,linesFile3)
def chaos_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "chaos_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_fc_chaos.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_chaos.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Chaos",linesFile1,linesFile2,linesFile3)

def richard_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "richard_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_richard.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_richard.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Richard",linesFile1,linesFile2,linesFile3)

def richard_trans_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "richard_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_richard.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_richard.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Richard",linesFile1,linesFile2,linesFile3)
def monte_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "monte_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_monte.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_monte.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Monte",linesFile1,linesFile2,linesFile3)
def pdf_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "zebra_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_pdf.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_pdf.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Pdf",linesFile1,linesFile2,linesFile3)
def benchfirst_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "benchfirst_bit.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "bechfirst_log.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_benchfirst.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Benchfirst",linesFile1,linesFile2,linesFile3)
def cpu_time_cast_bit():
    file1 = open(os.path.join(PATH, "datasets", "MY_CPU_bits.txt"), 'r')
    #file1=open('pascal_bits.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_cpu_new.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    file3 = open(os.path.join(PATH, "datasets", "fc_nli_cpu.txt"), 'r')
    linesFile3 = file3.readlines()
    return processData("Benchfirst",linesFile1,linesFile2,linesFile3)
def loadthebBenchmarks(benchmarks):
    bit_dicts=[]
    time_dicts=[]
    cast_cost_dics=[]
    for benchmark in benchmarks:
        if benchmark=="Raytrace":
            bit_dict,time_dict,cast_cost_dic=raytrace()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
        elif benchmark=='Scimark':
            bit_dict,time_dict,cast_cost_dic=scimark()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
        elif benchmark=='Pascal':
            bit_dict,time_dict,cast_cost_dic=pascal()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
        elif benchmark=='Sieve':
            bit_dict,time_dict,cast_cost_dic=sieve_time_cast_bit()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
        elif benchmark=='Nbody':
            bit_dict,time_dict,cast_cost_dic=nbody_time_cast_bit()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
        elif benchmark=='Meteor':
            bit_dict,time_dict,cast_cost_dic=meteor_time_cast_bit()
            bit_dicts.append(bit_dict)
            time_dicts.append(time_dict)
            cast_cost_dics.append(cast_cost_dic)
    return bit_dicts,time_dicts,cast_cost_dics
def loadthebBenchmark_trainsient(benchmark):
    if benchmark=="Raytrace":
        bit_dict,time_dict,cast_cost_dic=raytrace_trans()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Scimark':
        bit_dict,time_dict,cast_cost_dic=scimark_trans()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Pascal':
        bit_dict,time_dict,cast_cost_dic=trans_pascal()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Sieve':
        bit_dict,time_dict,cast_cost_dic=sieve_trans_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Nbody':
        bit_dict,time_dict,cast_cost_dic=nbody_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Meteor':
        bit_dict,time_dict,cast_cost_dic=meteor_trans_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=="Chaos":
        bit_dict,time_dict,cast_cost_dic=chaos_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Richard':
        bit_dict,time_dict,cast_cost_dic=richard_trans_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Monte':
        bit_dict,time_dict,cast_cost_dic=monte_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Pdf':
        bit_dict,time_dict,cast_cost_dic=pdf_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Benchfirst':
        bit_dict,time_dict,cast_cost_dic=benchfirst_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=="Cpu":
        bit_dict,time_dict,cast_cost_dic=cpu_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic

def loadthebBenchmark(benchmark):
    if benchmark=="Raytrace":
        bit_dict,time_dict,cast_cost_dic=raytrace()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Scimark':
        bit_dict,time_dict,cast_cost_dic=scimark()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Pascal':
        bit_dict,time_dict,cast_cost_dic=pascal()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Sieve':
        bit_dict,time_dict,cast_cost_dic=sieve_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Nbody':
        bit_dict,time_dict,cast_cost_dic=nbody_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Meteor':
        bit_dict,time_dict,cast_cost_dic=meteor_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=="Chaos":
        bit_dict,time_dict,cast_cost_dic=chaos_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Richard':
        bit_dict,time_dict,cast_cost_dic=richard_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Monte':
        bit_dict,time_dict,cast_cost_dic=monte_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Pdf':
        bit_dict,time_dict,cast_cost_dic=pdf_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=='Benchfirst':
        bit_dict,time_dict,cast_cost_dic=benchfirst_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
    elif benchmark=="Cpu":
        bit_dict,time_dict,cast_cost_dic=cpu_time_cast_bit()
        return bit_dict,time_dict,cast_cost_dic
if __name__ == "__main__":

    bit_dict,time_dict,cast_cost_dic=pascal()
    print(len(bit_dict),len(time_dict),len(cast_cost_dic))