import numpy as np
def find_euclidean(x1,x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def find_majority(lst):
    d = {}
    for ele in lst:
        if ele in d:
            d[ele]+=1
        else:
            d[ele] = 1
    return max(d, key = d.get)

class KNN:
    '''

    '''

    def __init__(self,k = 3):
        # keeping default 3 neighbours
        self.k = k

    def fit(self,X_train,Y_train):
        #there is no training in knn
        self.x_train = X_train
        self.y_train = Y_train

    def condensed():
        pass

    def predict(self, X):
        y_pred = [self.predict_(x) for x in X]
        return np.array(y_pred)

    def predict_(self,X):
        #calculating euclidean distance from all training points from x
        distance = [find_euclidean(X,x_train) for x_train in self.x_train]
        #sorting the distances and returning the indexes
        indexes = np.argsort(distance)
        # Selecting k number of neighbours
        k_neigh = indexes[:self.k]
        # extract the labels
        k_neigh_labels = [self.y_train[i] for i in k_neigh]
        # majority voting (selecting the label occuring the most times)
        label = find_majority(k_neigh_labels)
        return label

    def accuracy(self,y_pred,y_true):
        return (np.sum(y_pred == y_true))/len(y_true)
