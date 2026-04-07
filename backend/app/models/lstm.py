import torch.nn as nn
class TradingLSTM(nn.Module):
  def __init__(self): super().__init__(); self.lstm = nn.LSTM(10, 64)
  def forward(self, x): return self.lstm(x)