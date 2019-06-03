#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:46:41 2019

@author: xiangshuyang
"""
import numpy as np
import pandas as pd 
class regTree():
    def __init__(self,X,tolS,tolN):
        self.X=X
        self.tolS=tolS
        self.tolN=tolN
        
        
    def split(self,j,value):
        X=self.X
        X0= X[np.nozero(X[:,j]>value[0])[0],:]
        X1 = X[np.nozero(X[:,j]<=value[0])[0],:]
        return X0,X1
    
    def Leaf(self,Y):   # return the mean value of the output
        return np.sum(Y) 
    
    def Error(self,Y): # return the toal variance  of the output 
        Y=np.matrix(Y)
        return np.var(Y)*np.shape(Y)[0]
    
    def choosebestsplit(self):
        tolS=self.tolS
        tolN=self.tolN
        X=np.matrix(self.X)
        m,n=np.shape(X)
        error=self.Error(X[:-1])
        besterror= 10**(16)
        for j in range(n-1):
            for splitval in set(X[:j]): 
             X0,X1=self.split(X,j,splitval)  
             if np.shape(X0)[0]<tolN or np.shape(X1)[0]<tolN:
                 continue
             error_temp= self.Error(X0[:,-1]+X1[:,-1])
             if error_temps<besterror :
                 bestindex=j 
                 bestvalue=splitvalue 
                 besterror=error_temps
        if (error-besterror)<tolS:
            return None, self.Leaf(X[:,-1])
        X0,X1=self.split(X,bestindex,bestvalue) 
        if np.shape(X0)[0]<tolN or np.shape(X1)[0]<tolN:
            return None, self.Leaf(X[:,-1])
        return bestvalue, self.Leaf(X[:,-1])
                 
             
             
 ######load the data########
def loaddata(filename):
    data=[]
    fr=open(filename)
    for line in fr.readlines():
        arrline= line.strip().split('\t')
        floline= map(float,arrline)
        data.append(floline)
        
    return data


#####test########
data=loaddata('regressiontree.txt')          
g=regTree(data,1,4) 
g.choosebestsplit()
           
    
    

    
