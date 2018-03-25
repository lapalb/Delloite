import numpy as numpy
import pandas as pd
df=pd.read_csv("Delo.csv")
df.describe()
df.shape
def pre():
    global PL17  #PRIORITY_LOAD_1 On Day7
    global PL27  #PRIORITY_LOAD_2 On Day7
    global PL37  #PRIORITY_LOAD_3 On Day7
    global PL47  #PRIORITY_LOAD_4 On Day7
    global required_power # Predicted Power on On Day 7 using Simple Linear Regression
    global generated_power #Generated Power On Day 7
    global deficit #Deficit on Day 7
    PL17=(df['PL1-0']+df['PL1-1']+df['PL1-2']+df['PL1-3']+df['PL1-4']+df['PL1-5']+df['PL1-6'])/((df.shape[1]-1)/4)
    PL27=(df['PL2-0']+df['PL2-1']+df['PL2-2']+df['PL2-3']+df['PL2-4']+df['PL2-5']+df['PL2-6'])/((df.shape[1]-1)/4)
    PL37=(df['PL2-0']+df['PL3-1']+df['PL4-2']+df['PL3-3']+df['PL3-4']+df['PL3-5']+df['PL3-6'])/((df.shape[1]-1)/4)
    PL47=(df['PL4-0']+df['PL4-1']+df['PL4-2']+df['PL4-3']+df['PL4-4']+df['PL4-5']+df['PL4-6'])/((df.shape[1]-2)/4)
    required_power=sum(PL17+PL27+PL37+PL47)
pre()

def output():
    print("The Predicted load on day 7 is: ")
    print(sum(PL17))
    print(sum(PL27))
    print(sum(PL37))
    print(sum(PL47))
    print("The required Power will be:",required_power)
output()

generated_power=input("Enter the Generated Power")
deficit=required_power-float(generated_power)
print("The Deficit is:" , deficit)

def solve():
    if(deficit>0):
        if(sum(PL47)>deficit):
            print("Cut the P4 Load")
        elif ((sum(PL47)+sum(PL37))>deficit):
            print("Cut the P3 Load and P4 LOAD")
        elif ((sum(PL47)+sum(PL37)+sum(PL27))>deficit):
            print("Cut the P2,P3 and P4 Load")
        else:
            print("Cant stop Outage")
    else:
        print("No Outage! Enjoy the Power:)")
solve() 