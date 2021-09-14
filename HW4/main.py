#================================ Q1.0 ================================
print('#================================ Q1 ================================')
import math
import csv

#================================ Q1.1 ================================
point = [1, 0, 0, '?'] 
data1 = [1, 1, 1, 'M']
data2 = [1, 2, 0, 'F']

#================================ Q1.2 ================================

def printVector(vec):
    print('The vector ',vec[:-1],' has tag ',vec[-1])

printVector(data1)
printVector(data2)

#================================ Q1.3 ================================
def euclideanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         #print ('x is ' , x)
         num1=float(instance1[x])
         num2=float(instance2[x])
         distance += pow(num1-num2, 2)
   return math.sqrt(distance)

print('Distance between vectors: ',euclideanDistance(data1,data2,len(data2)-1),'\n')

#================================ Q1.4 ================================
with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile.csv', 'r') as myCsvfile:
    lines = csv.reader(myCsvfile)
    dataWithHeader = list(lines)

#put data in dataset without header line
dataset = dataWithHeader[1:]

printVector(dataset[0])
printVector(dataset[1])
distance = euclideanDistance(dataset[0],dataset[1],len(dataset[1])-1)
print('Distance between vectors: ',distance,'\n')

#================================ Q1.5 ================================
class distClass:
    dist = -1 #distance of current point from test point
    tag = '-' #tag of current point

eucDistances = [] # list of distances, will hold objects of type distClass

point = dataset[0]

for vec in dataset[1:]:
    obj = distClass()
    distance = euclideanDistance(point, vec, len(vec)-1)
    obj.dist = distance
    obj.tag = vec[-1]
    eucDistances.append(obj)

#================================ Q1.6 ================================
eucDistances.sort(key=lambda x: x.dist) 

#================================ Q1.7 ================================
print("Point: ",point[:-1]) # print the point to calculate distance from

for vec in dataset[1:]:
    print(vec[:-1],' Distance: ',euclideanDistance(point, vec, len(vec)-1))

#================================ Q1.8 ================================
print('\nFor K=1 the tag is: ',eucDistances[0].tag,'\n')

#================================ Q1.9 ================================
tagCounterM = 0
tagCounterF = 0

for i in range(3):
    if eucDistances[i].tag == 'M':
        tagCounterM += 1
    if eucDistances[i].tag == 'F':
        tagCounterF += 1

if tagCounterM >= 2:
    print('\nFor K=3 the tag is: M\n')

elif tagCounterF >= 2:
    print('\nFor K=3 the tag is: F\n')

else:
    print("ERROR\nInsufficent Information\n")

#================================ Q2.1 ================================
print('#================================ Q2 ================================')
K = 3

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile.csv', 'r') as myCsvfileSrc:
    lines1 = csv.reader(myCsvfileSrc)
    dataWithHeader1 = list(lines1)

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile_test.csv', 'r') as myCsvfileDst:
    lines2 = csv.reader(myCsvfileDst)
    dataWithHeader2 = list(lines2)

for point in dataWithHeader2[1:]:

    eucDistances = [] # list of distances, will hold objects of type distClass

    for vec in dataWithHeader1[1:]:
        obj = distClass()
        distance = euclideanDistance(point, vec, len(vec)-1)
        obj.dist = distance
        obj.tag = vec[-1]
        eucDistances.append(obj)

    eucDistances.sort(key=lambda x: x.dist) 

    tagCounterM = 0
    tagCounterF = 0

    for i in range(K):
        if eucDistances[i].tag == 'M':
            tagCounterM += 1
        if eucDistances[i].tag == 'F':
            tagCounterF += 1

    if tagCounterM > K//2:
        print('\nFor K=3 the tag is: M\n')

    elif tagCounterF > K//2:
        print('\nFor K=3 the tag is: F\n')

    else:
        print("ERROR\nInsufficent Information\n")