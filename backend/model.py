# adapted from https://www.geeksforgeeks.org/linear-regression-using-pytorch/

import torch

model_path_name = "model.pt"

class LinearRegressionModel(torch.nn.Module):
 
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
    
    def score(self):
        return self.linear