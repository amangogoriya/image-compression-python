import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self,K):
        self.K = K

    def findClosestCentroids(self,X,centriods):
        """ this function will return the idx of closest distance from centriods """
        m,n = X.shape
        k = len(centriods)
        idx =  np.zeros((m,1))
        for i in range(m):
            displaydata = np.zeros((1,self.K))
            for j in range(k):
                 displaydata[:,j] = np.sqrt(np.sum(np.power((X[i,:]-centriods[j,:]),2)))
            idx[i] = np.argmin(displaydata)+1
        return idx


    def computeCentroids(self,X,idx):
        m,n = X.shape
        centroids = np.zeros((self.K,n))
        count = np.zeros((self.K,1))
        for i in range(m):
            index = int(idx[i]-1)
            centroids[index,:] += X[i,:]
            count[index]+=1
        return centroids/count


    def kMeansInitCentroids(self,X):
        m,n = X.shape
        centriod = np.zeros((self.K,n))
        for i in range(self.K):
            centriod[i] = X[np.random.randint(0,m+1),:]
        return centriod

    def runKmeans(self,X,centroid,num_iter):
        idx = self.findClosestCentroids(X,centroid)
        for i in range(num_iter):
            centroid =  self.computeCentroids(X,idx)
            idx = self.findClosestCentroids(X,centroid)
        return centroid,idx
