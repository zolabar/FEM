import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
#########################################
#
# Dr. Zoufine Lauer-Bare, DHBW Karlsruhe
# Simulationstechnik/FEM
#
#########################################


# Drei innere Knoten         
    
    
def N(x,i):
    
    if i==0:
        if x >=0 and x<0.5:
            wert=1-2*x
        else:
            wert=0
    elif i==2:
        if x >3/2. and x<=2:
            wert=2*(x-3/2.)
        else:
            wert=0
    else:
        if x >=i-1/2. and x<i:
            wert=2*(x-(i-1/2.))
        elif x>=i and x<i+1/2.:
             wert=1-2*(x-i)        
        else:
            wert=0
        
    return wert        
    
    

def Nh(x,i):

    NF=[]
    for j in x:
        NF.append(N(i,j))
        
    return np.asarray(NF)  
    
    
    
# Fuenf innere Knoten      


def N5(i,x):
    
    if i==0:
        if x >=0 and x<1/3.:
            wert=1-3*x
        else:
            wert=0
    elif i==2:
        if x >5/3. and x<=2:
            wert=3*(x-5/3.)
        else:
            wert=0
    else:
        if x >=i-1/3. and x<i:
            wert=3*(x-(i-1/3.))
        elif x>=i and x<i+1/3.:
             wert=1-3*(x-i)        
        else:
            wert=0    
            
            
    return wert        
                

                               
                
def Nh5(x,i):

    NF=[]
    for j in x:
        NF.append(N5(i,j))
        
    return np.asarray(NF)  