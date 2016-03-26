__author__ = 'AliOsman & Emrullah'
import math
from functions import functions
class KMEANS:

    @staticmethod
    def KMeans(data,classterCount,globalCounter):
        counter=0
        classes=[]
        cluster =[[]]
        cluster_index=[]
        tempClasses=[]
        for i in range(0,classterCount):
            globalCounter+=1
            classes.append(cluster)
            cluster_index.append(cluster)
            tempClasses.append(cluster)
        classes2=classes[:]
        for i in range(0,len(classes)):
            globalCounter=1
            cluster = [data[i]]
            classes[i]=cluster
        functions.ResetClasterIndex(cluster_index,classterCount,globalCounter)
        functions.ResetClasterIndex(classes2,classterCount,globalCounter)
        def clusterFills(classeses,globalCounter,counter):
            counter+=1
            combinedOfClasses = functions.CopyTo(classeses)
            functions.ResetClasterIndex(cluster_index,classterCount,globalCounter)
            functions.ResetClasterIndex(tempClasses,classterCount,globalCounter)
            avarage=[]
            for k in range(0,len(combinedOfClasses)):
                globalCounter+=1
                avarage.append(functions.GetAvarage(combinedOfClasses[k]))
            for i in range(0,len(data)):
                globalCounter+=1
                minimum=0
                index=0
                for k in range(0,len(avarage)):
                    total=0.0
                    for j in range(0,len(avarage[k])):
                        total += (avarage[k][j]-data[i][j]) **2
                    tempp=math.sqrt(total)
                    if(k==0):
                        minimu=tempp
                    if(tempp<=minimu):
                        minimu=tempp
                        index=k
                tempClasses[index].append(data[i])
                cluster_index[index].append(i)
            if(functions.CompareArray(tempClasses,combinedOfClasses)==1):
                return clusterFills(tempClasses,globalCounter,counter)
            returnArray = []
            returnArray.append(tempClasses)
            returnArray.append(cluster_index)
            returnArray.append(avarage)
            returnArray.append(counter)
            return returnArray

        cdcd = clusterFills(classes,globalCounter,counter)
        if cdcd !=None:
            return cdcd

    @staticmethod
    def KMeansPer(data,classterCount,globalCounter):
        perData=data[0:int(float(len(data))/100*30)]
        result = KMEANS.KMeans(perData,classterCount,globalCounter)
        cluster_index=[]
        tempClasses=[]
        classes=[]
        cluster =[[]]
        for i in range(0,classterCount):
            globalCounter+=1
            classes.append(cluster)
            cluster_index.append(cluster)
            tempClasses.append(cluster)
        classes2=classes[:]
        for i in range(0,len(classes)):
            globalCounter=1
            cluster = [data[i]]
            classes[i]=cluster
        functions.ResetClasterIndex(cluster_index,classterCount,globalCounter)
        functions.ResetClasterIndex(classes2,classterCount,globalCounter)
        counter=0
        def clusterFills(classeses,globalCounter,counter):
            counter+=1
            combinedOfClasses = functions.CopyTo(classeses)
            functions.ResetClasterIndex(cluster_index,classterCount,globalCounter)
            functions.ResetClasterIndex(tempClasses,classterCount,globalCounter)
            avarage=[]
            for k in range(0,len(combinedOfClasses)):
                globalCounter+=1
                avarage.append(functions.GetAvarage(combinedOfClasses[k]))
            for i in range(0,len(data)):
                globalCounter+=1
                minimum=0
                index=0
                for k in range(0,len(avarage)):
                    total=0.0
                    for j in range(0,len(avarage[k])):
                        total += (avarage[k][j]-data[i][j]) **2
                    tempp=math.sqrt(total)
                    if(k==0):
                        minimu=tempp
                    if(tempp<=minimu):
                        minimu=tempp
                        index=k
                tempClasses[index].append(data[i])
                cluster_index[index].append(i)
            if(functions.CompareArray(tempClasses,combinedOfClasses)==1):
                return clusterFills(tempClasses,globalCounter,counter)
            returnArray = []
            returnArray.append(tempClasses)
            returnArray.append(cluster_index)
            returnArray.append(avarage)
            returnArray.append(counter)
            return returnArray

        cdcd = clusterFills(result[0],globalCounter,counter)
        if cdcd !=None:
            return cdcd
