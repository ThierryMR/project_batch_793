class Trainer():
    def __init__(self):
        self.X = None 
        
    def trainer(self, X, model):
        prediciton = model.predict(X)
        return prediciton