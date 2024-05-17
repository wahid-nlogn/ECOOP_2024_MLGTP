import datasets.data_loader as data_loader
import torch
import numpy as np
from torch_geometric.data import Data, DataLoader
def genrateGraphDataSet(X,y,call_graph,dictionary):
    edge = []

    edge_atribute={}
    for key in call_graph:
        for val in call_graph[key]:
            edge.append([dictionary[key], dictionary[val[0]]])
            edge_atribute[(dictionary[key], dictionary[val[0]])]=val[1]

    edge_info=[]
    edge_atr=[]
    for e in edge:
        edge_atr.append([edge_atribute[(e[0],e[1])]])
    for i in range(len(edge[0])):
        temp=[]
        for j in range(len(edge)):
            temp.append(edge[j][i])
        edge_info.append(temp)



    int_to_str = {}
    for key in dictionary:
        int_to_str[dictionary[key]] = key
    #print(int_to_str)
    node = []
    for x in X:
        temp = []
        for key in range(len(dictionary)):
            temp.append(x[int_to_str[key]])
        node.append(temp)

    X_node = np.array(node)
    y=np.array(y).reshape(-1, 1)
    temp_xnode=np.array(node)
    temp_xnode=np.reshape(temp_xnode,(X_node.shape[0],X_node.shape[1],1))
    print(X_node.shape,temp_xnode.shape)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    train_pos_edge_index = torch.tensor(np.array(edge_info), dtype=torch.long).to(device)
    graph_edge_atr=torch.tensor(np.array(edge_atr), dtype=torch.long).to(device)
    graph_edge_atr=np.reshape(graph_edge_atr,(len(graph_edge_atr),1))
    data_set = []
    for i in range(len(y)):
        data = Data(x=torch.from_numpy(temp_xnode[i]).float().to(device),
                    edge_index=train_pos_edge_index,
                    edge_attr=graph_edge_atr,
                    y=torch.from_numpy(y[i]).float().to(device))
        data_set.append(data)

    return data_set
def genrarate_raytrace_graph():
    X, y, call_graph, dictionary = data_loader.raytrace()
    print("Function name numbering: ", dictionary)
    return genrateGraphDataSet(X,y,call_graph,dictionary)
def generate_pascal_graph():
    X, y, call_graph, dictionary = data_loader.pascal_matrix()
    print("Function name numbering: ", dictionary)
    return genrateGraphDataSet(X, y, call_graph, dictionary)

if __name__ == "__main__":
    generate_pascal_graph()