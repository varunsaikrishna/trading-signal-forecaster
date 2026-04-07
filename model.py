import torch
import torch.nn as nn
class LSTMForecaster(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=10, hidden_size=64)
    def forward(self, x):
        return self.lstm(x)