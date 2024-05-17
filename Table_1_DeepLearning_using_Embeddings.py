import sys
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch.utils.data import random_split


# adding the parent directory to
# the sys.path.

directory_path="benchmarks_embeddings"

file_paths =[]

class MyDataset(Dataset):
    def __init__(self, file_paths):
        self.data = []
        for file_path in file_paths:
            loaded_data = torch.load(file_path)
            self.data.extend(loaded_data)  # Assuming loaded_data is a list of (tensor, scalar) pairs

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        tensor, runtime = self.data[idx]
        return tensor, runtime
    @staticmethod
    def accuracy(y_pred, y_test, threshold=0.1):
        correct = ((y_pred - y_test).abs() < threshold).sum().item()
        total = len(y_test)
        return correct / total

    @staticmethod
    def mean_absolute_error(y_pred, y_test):
        return torch.mean(torch.abs(y_pred - y_test)).item()

    @staticmethod
    def mean_squared_error(y_pred, y_test):
        return torch.mean((y_pred - y_test)**2).item()
    
    @staticmethod
    def error_ratio_percentage(y_pred, y_test):
        error = torch.mean(torch.abs(y_pred - y_test) / y_test).item()
        return error * 100  # Convert error ratio to percentag
for file in os.listdir(directory_path):
    if file.endswith(".pt"):
        file_paths.append(directory_path+'/'+file) 
#my_dataset = MyDataset(file_paths)
print(file_paths)
batch_size = 64  # Set your desired batch size


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(4 * 768, 512)  # Adjust input size based on your tensor shape
        self.fc2 = nn.Linear(512, 256)
        self.fc3=nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 1)  # Output size for regression (1 for scalar output)

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten the input tensor
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.fc4(x)
        return x
model = MyModel()


for index,file in enumerate(file_paths):
    my_dataset = MyDataset(file_paths[0:index]+file_paths[index+1:])
    #train_size = int(train_size_per * len(my_dataset))
    #test_size = len(my_dataset) - train_size
    my_testdaset=MyDataset([file])

    # Split the dataset into training and testing sets
    #train_dataset, test_dataset = random_split(my_dataset, [train_size, test_size])
    train_dataset, test_dataset=my_dataset,my_testdaset
    # Create DataLoaders for training and testing sets
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)



    #my_dataloader = DataLoader(my_dataset, batch_size=batch_size, shuffle=True)
    #print("My data loader length:",len(my_dataloader))


    # Define loss function and optimizer
    criterion = nn.MSELoss()  # Mean Squared Error for regression
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    num_epochs = 10  # Define number of epochs
    for epoch in range(num_epochs):
        for X_batch, Y_batch in train_dataloader:
            # Forward pass
            outputs = model(X_batch)

            # Compute loss
            loss = criterion(outputs.squeeze(), Y_batch.float())

            # Zero gradients, backward pass, and optimizer step
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Print training progress
            #print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    error_ratios=[]
    model.eval()
    maes=[]
    rses=[]
    with torch.no_grad():
        for X_batch, Y_batch in test_dataloader:
            # Forward pass to get predictions
            predictions = model(X_batch)
            
            # Evaluate predictions (perform any evaluation metrics calculation here)
            acc = MyDataset.accuracy(predictions, Y_batch)
            mae = MyDataset.mean_absolute_error(predictions, Y_batch)
            mse = MyDataset.mean_squared_error(predictions, Y_batch)
            #error_r = MyTestDataset.error_ratio(predictions, Y_batch)
            error_r_percentage = MyDataset.error_ratio_percentage(predictions, Y_batch)  # Calculate error ratio in percentage

            """print(f"Accuracy: {acc}")
            print(f"MAE: {mae}")
            print(f"MSE: {mse}")
            #print(f"Error Ratio: {error_r}")
            print(f"Error Ratio (Percentage): {error_r_percentage}%")"""
            error_ratios.append(error_r_percentage)
            maes.append(mae)
            rses.append(mse)

    print("===========================================================")
    print("Benchmark:",file, "Train dataset: ",len(train_dataset),"Test dataset: ",len(test_dataset))
    print("Error ratios",sum(error_ratios)/len(error_ratios))
    print("MAE: ", sum(maes)/len(maes))
    print("MSE: ", sum(rses)/len(rses))
    print("===========================================================")




# ========================== TESTING ===================================
class MyTestDataset(Dataset):
    def __init__(self, file_paths):
        self.data = []
        for file_path in file_paths:
            loaded_data = torch.load(file_path)
            self.data.extend(loaded_data)  # Assuming loaded_data is a list of (tensor, scalar) pairs

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        tensor, runtime = self.data[idx]
        return tensor, runtime

    @staticmethod
    def accuracy(y_pred, y_test, threshold=0.1):
        correct = ((y_pred - y_test).abs() < threshold).sum().item()
        total = len(y_test)
        return correct / total

    @staticmethod
    def mean_absolute_error(y_pred, y_test):
        return torch.mean(torch.abs(y_pred - y_test)).item()

    @staticmethod
    def mean_squared_error(y_pred, y_test):
        return torch.mean((y_pred - y_test)**2).item()
    
    @staticmethod
    def error_ratio_percentage(y_pred, y_test):
        error = torch.mean(torch.abs(y_pred - y_test) / y_test).item()
        return error * 100  # Convert error ratio to percentag

# Example usage:
#test_dataset = MyTestDataset(file_paths)
#test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

