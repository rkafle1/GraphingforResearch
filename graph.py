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

def GenerateBarGraphCompare(y1, y2):
    xdata = []
    y1data = []
    y2data = []
    with open('UCTransferData.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            xdata.append(row[0])
            y1data.append(row[y1])
            y2data.append(row[y1])
    
    for i in range(1, len(y1data)):
        y1data[i] = float(y1data[i])
        y2data[i] = float(y2data[i])
    plt.bar(xdata[1:], y1data[1:], width = 0.5,label = "Universitiesvs." + y1data[0] +
     "vs"+ y2data[0])
    plt.bar(xdata[1:], y2data[1:], width = 0.5,label = "Universitiesvs." + y1data[0] +
     "vs"+ y2data[0])
    plt.xlabel('Universities')
    plt.ylabel(y1data[0])
    plt.title("Universitiesvs." + y1data[0] + "vs"+ y2data[0])
    plt.legend()
    plt.savefig("Universitiesvs." + y1data[0] +"vs"+ y2data[0]+ ".png")
    plt.close()
GenerateBarGraphCompare(1,2)