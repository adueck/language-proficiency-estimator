import torch
from torch.autograd import Variable
from model import LinearRegressionModel, model_path_name

model = LinearRegressionModel()
model.load_state_dict(torch.load(model_path_name))

def query_model(age, education, percent):
  dependants = Variable(torch.Tensor([[age, education, percent]]))
  return min(round(model(dependants).item()), 98)