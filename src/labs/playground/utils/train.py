from keras.layers import LSTM

class BaseTraing:
    
    def __init__(self, *args, **kwargs):
        pass
    
    def train(self, *args, **kwargs):
        pass
    
    def add_node(self, signal: float, weight: float, bias: float, *args, **kwargs) -> [float]:
        return [.0]