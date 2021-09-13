import math
import csv

class distClass:
    dist = -1 #distance of current point from test point
    tag = '-' #tag of current point

def printVector(vec):
    print('The vector ',vec[:-1],' has tag ',vec[-1])

def euclideanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         #print ('x is ' , x)
         num1=float(instance1[x])
         num2=float(instance2[x])
         distance += pow(num1-num2, 2)
   return math.sqrt(distance)

point = [1, 0, 0, '?'] 
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']

printVector(data1)
printVector(data2)

print('Distance between vectors: ',euclideanDistance(data1,data2,3),'\n')

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile.csv', 'r') as myCsvfile:
    lines = csv.reader(myCsvfile)
    dataWithHeader = list(lines)

#put data in dataset without header line
dataset = dataWithHeader[1:]

printVector(dataset[0])
printVector(dataset[1])
distance = euclideanDistance(dataset[0],dataset[1],3)
print('Distance between vectors: ',distance,'\n')
obj = distClass()

eucDistances = [] # list of distances, will hold objects of type distClass
obj.dist = distance
obj.tag = dataset[1][-1]
eucDistances.append(obj)

print(type(obj))