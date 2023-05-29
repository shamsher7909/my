#------------------------------------------------------------------------
# Regression model generated by GeneXproTools 5.0 on 6/12/2021 3:17:10 PM
# GEP File: D:\Kunsan Uni\tP\Simulation\Combined.gep
# Training Records:  170
# Validation Records:   84
# Fitness Function:  RMSE
# Training Fitness:  20.0333000899046
# Training R-square: 0.767648651597832
# Validation Fitness:   9.12109947795283
# Validation R-square:  0.173218051120634
#------------------------------------------------------------------------

from math import *

def gepModelF(d):

    G1C2 = 2.44813326436314
    G2C4 = -5.96404343284189
    G3C8 = 2.23081384754204
    G3C6 = -12.6999197173224
    G4C2 = 9.84874913785211
    G4C1 = -10.7899129249545
    G5C3 = 13.6500954286159
    G5C9 = -8.99609149449141

    L = 0
    DD = 1
    i = 2
    phi = 3
    sigma_v = 4

    y = 0.0

    y = (((max((d[sigma_v]/d[phi]),G1C2)*(1.0-d[L]))+((d[sigma_v]/d[L])-((d[phi]+d[L])/2.0)))/2.0)
    y = y + max(d[L],(((d[i]*d[L])-max(d[sigma_v],d[i]))/((G2C4+d[L])*d[L])))
    y = y + (gep3Rt(((d[sigma_v]-d[phi])*pow(d[phi],2.0)))-((G3C8-d[L])*((G3C6+d[phi])/2.0)))
    y = y + pow((d[DD]-(((((d[L]+d[phi])/2.0)+max(G4C1,G4C1))/2.0)*(G4C2*d[DD]))),2.0)
    y = y + ((min((d[i]+G5C9),d[L])+(d[sigma_v]-d[DD]))/((d[L]*G5C3)-(d[i]+d[sigma_v])))

    return y
    

def gep3Rt(x):
    if (x < 0.0):
        return -pow(-x,(1.0/3.0))
    else:
        return pow(x,(1.0/3.0))