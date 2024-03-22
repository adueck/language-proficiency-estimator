# adapted from https://www.geeksforgeeks.org/linear-regression-using-pytorch/

from best import x_data, y_data
import numpy as np
from sklearn import linear_model
import torch
from torch.autograd import Variable
from model import LinearRegressionModel, model_path_name

# convert data arrays to torch.Tensor for training
x_data_t = Variable(torch.Tensor(x_data))
y_data_t = Variable(torch.Tensor(y_data))

X = np.array(x_data)
Y = y_data
    
model = LinearRegressionModel()

criterion = torch.nn.MSELoss(size_average = False)
optimizer = torch.optim.SGD(model.parameters(), lr = 1e-8)

# train model
for epoch in range(100000):
    # Forward pass: Compute predicted y by passing 
    # x to the model
    pred_y = model(x_data_t)
 
    # Compute and print loss
    loss = criterion(pred_y, y_data_t)
 
    # Zero gradients, perform a backward pass, 
    # and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('epoch {}, loss {}'.format(epoch, loss.item()))

print(model.score())
print("Saving model at " + model_path_name)
# save model
torch.save(model.state_dict(), model_path_name)

# get R2 score
ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
score = model.score(X, Y)
print(f'R2 score is {score}')
