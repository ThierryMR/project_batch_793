from statistics import LinearRegression


class Trainer():
    def __init__(self):
        self.X = None 
        
    def trainer(self, X, model):
        prediciton = model.predict(X)
        return prediciton
    
    def create_model(self):
        model = LinearRegression()
        return model