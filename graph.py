import csv
import matplotlib.pyplot as plt
import pandas as pd
# enter indices from CSV file you want to graph to compare between universities
def GenerateBarGraphUniversity(y): 
    xdata = []
    ydata = []
    with open('UCTransferData.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            xdata.append(row[0])
            ydata.append(row[y])
    
    for i in range(1, len(ydata)):
        ydata[i] = float(ydata[i])
    plt.bar(xdata[1:], ydata[1:], width = 0.72,label = "Universitiesvs." + ydata[0])
    plt.xlabel('Universities')
    plt.ylabel(ydata[0])
    plt.title("Universitiesvs." + ydata[0])
    plt.legend()
    plt.savefig("Universitiesvs." + ydata[0] + ".png")
    plt.close()

for i in range(1, 6):
    GenerateBarGraphUniversity(i)