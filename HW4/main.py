#================================ Q1.0 ================================
print('#================================ Q1 ================================')
import math
import csv
import copy      # need for deep copy in Q2.2

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
def checkAccurancy(data1, data2):
    countAccurent = 0
    for i in range(len(data1)):
        if data1[i][-1] == data2[i][-1]:
            countAccurent += 1
    return (countAccurent/len(data1))

print('#================================ Q2.1 ================================')
K = 3

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile.csv', 'r') as myCsvfileSrc1:
    lines1 = csv.reader(myCsvfileSrc1)
    dataWithHeader1 = list(lines1)

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile_test.csv', 'r') as myCsvfileSrc2:
    lines2 = csv.reader(myCsvfileSrc2)
    dataWithHeader2 = list(lines2)

data = copy.deepcopy(dataWithHeader2)

for point in data[1:]:

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
        #print('\nFor K=3 the tag is: M\n')
        point[-1]='M'

    elif tagCounterF > K//2:
        #print('\nFor K=3 the tag is: F\n')
        point[-1]='F'

    else:
        #print("ERROR\nInsufficent Information\n")
        point[-1]='?'

with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/myFile_testOutput.csv', 'w', newline='') as myCsvfileDst:
    writer = csv.writer(myCsvfileDst)
    writer.writerows(dataWithHeader2)

print('Accurency: ',checkAccurancy(dataWithHeader2[1:],data[1:])*100,'%')


#================================ Q2.2 ================================
#======================= Q2.2a-d =======================
# Q2.2a For K=1 the accurency is 50.0 %
# Q2.2b For K=7 the accurency is 74.0 %
# Q2.2c For K=19 the accurency is 68.0 %
# Q2.2d K=7 came out the best with 74.0 % accurency

print('#================================ Q2.2 ================================')

def knn_csv_output(K, distanceFunc, dstFileName):
    with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/mytrain.csv', 'r') as myCsvfileSrc1:
        lines1 = csv.reader(myCsvfileSrc1)
        dataWithHeader1 = list(lines1)

    
    
    with open('C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/mytest.csv', 'r') as myCsvfileSrc2:
        lines2 = csv.reader(myCsvfileSrc2)
        dataWithHeader2 = list(lines2)

    data = copy.deepcopy(dataWithHeader2)

    for point in data[1:]:

        Distances = [] # list of distances, will hold objects of type distClass

        for vec in dataWithHeader1[1:]:
            obj = distClass()
            distance = distanceFunc(point, vec, len(vec)-1)
            obj.dist = distance
            obj.tag = vec[-1]
            Distances.append(obj)

        Distances.sort(key=lambda x: x.dist) 

        tagCounterM = 0
        tagCounterF = 0

        for i in range(K):
            if Distances[i].tag == 'M':
                tagCounterM += 1
            if Distances[i].tag == 'F':
                tagCounterF += 1

        if tagCounterM > K//2:
            #print('\nFor K=3 the tag is: M\n')
            point[-1]='M'

        elif tagCounterF > K//2:
            #print('\nFor K=3 the tag is: F\n')
            point[-1]='F'

        else:
            #print("ERROR\nInsufficent Information\n")
            point[-1]='?'

    dstFilePath = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW4/' + dstFileName

    with open(dstFilePath, 'w', newline='') as myCsvfileDst:
        writer = csv.writer(myCsvfileDst)
        writer.writerows(data)

    print('Accurency: ',checkAccurancy(dataWithHeader2[1:],data[1:])*100,'%')

K = 1
knn_csv_output(K,euclideanDistance,'mytest1e.csv')

K = 7
knn_csv_output(K,euclideanDistance,'mytest7e.csv')

K = 19
knn_csv_output(K,euclideanDistance,'mytest19e.csv')

#======================= Q2.2e =======================
# Q2.2e 
# For K=1 the accurency is 61.0 %
# For K=7 the accurency is 63.0 %
# For K=19 the accurency is 70.0 %

def manhattanDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         num1=float(instance1[x])
         num2=float(instance2[x])
         distance += abs(num1-num2)
   return distance

K = 1
knn_csv_output(K,manhattanDistance,'mytest1m.csv')

K = 7
knn_csv_output(K,manhattanDistance,'mytest7m.csv')

K = 19
knn_csv_output(K,manhattanDistance,'mytest19m.csv')

#======================= Q2.2f =======================
# Q2.2f 
# For K=1 the accurency is 61.0 %
# For K=7 the accurency is 55.0 %
# For K=19 the accurency is 56.0 %

def hammingDistance(instance1, instance2, length):
   distance = 0
   for x in range(length):
         num1=float(instance1[x])
         num2=float(instance2[x])
         if num1 != num2:
            distance += 1
   return distance

K = 1
knn_csv_output(K,hammingDistance,'mytest1h.csv')

K = 7
knn_csv_output(K,hammingDistance,'mytest7h.csv')

K = 19
knn_csv_output(K,hammingDistance,'mytest19h.csv')

# Q2.2g
# Euclidean Distance with K=7 had the most accurency at 74.0 %