# coding=utf-8
__author__ = 'AliOsman & Emrullah'
import collections
import  sys
import math


sys.setrecursionlimit(10000)
class functions(object):

    @staticmethod
    def MainFieldsToFields(mainDataTableFields,dataTableFields,globalCounter): # Main Data Table Fields to Data Table Fields
        for i in range(0,len(mainDataTableFields)):
            dataTableFields.append(mainDataTableFields[i])
            globalCounter+=1
    @staticmethod
    def FillMainDataTable( mainDataTable, dataTable, ColumCount,globalCounter):  # Fill the Main Table by which Temp Table
        for i in range(0, ColumCount):
            column = []
            globalCounter+=1
            for row in dataTable:
                column.append(row[i])
                globalCounter+=1
            mainDataTable.append(column)
    @staticmethod
    def isfloat(value):
          try:
            float(value)
            return True
          except ValueError:
            return False
    @staticmethod
    def DistanceDataTable(mainDataTable,dataTable,dataTableFields,globalCounter): # Fill the Data Table as Distance by which Main Table
        deletedColums=[]
        willBeDeleted=[]
        for i in range(0,len(mainDataTable)):
            globalCounter+=1
            myDistince = list(set(mainDataTable[i]))
            try:
                float(myDistince[0])
                dataTable.append(mainDataTable[i])
            except:
                if((len(mainDataTable[i])!=len(myDistince) and len(myDistince)>=2)):
                    dataTable.append(mainDataTable[i])
                else:
                    willBeDeleted.append(i)
                    deletedColums.append([i,dataTableFields[i],myDistince])
        willBeDeleted.reverse()
        for k in range(len(willBeDeleted)): # Remove Field at Data Table Fields
            globalCounter+=1
            dataTableFields.pop(willBeDeleted[k])
        return deletedColums
    @staticmethod
    def SameDataDelete(dataTable,dataTableFields,globalCounter):
        willBeDeleted = []
        deletedColumn=[]
        for i in range(0,len(dataTable)):
            mostValue=0
            globalCounter+=1
            try:
                temp = float(collections.Counter(dataTable[i]).most_common(1)[0][0])
            except:
                mostValue=collections.Counter(dataTable[i]).most_common(1)[0][1]
            columnLenght=float(float(len(dataTable[i]))/100*90)
            if mostValue>columnLenght:
                willBeDeleted.append(i)
                deletedColumn.append([dataTableFields[i],mostValue,collections.Counter(dataTable[i]).most_common(1)[0][0]])
        willBeDeleted.reverse()  #gelen verileri tersine cevir
        for k in range(0,len(willBeDeleted)):
            globalCounter+=1
            dataTable.remove(dataTable[willBeDeleted[k]])
            dataTableFields.pop(willBeDeleted[k])
        return deletedColumn
    @staticmethod
    def FillMissingValues(dataTable,globalCounter,dataTableFields):#Fill the missing value at Data Table
        missingCount=[]
        for i in range(0,len(dataTable)):
            globalCounter+=1
            intCounter =0
            stringCounter=0
            intTotal=0
            for row in dataTable[i]:
                globalCounter+=1
                try:
                    test = float(row)
                    intCounter+=1
                    intTotal+=test # eger int değer çok ise boş bırakmak yerine ortalama basmak için topla sonra avarage al
                except:
                    stringCounter+=1
            if intCounter>0:
                columnLenght=len(dataTable[i])/100*80
                if columnLenght > intCounter:
                    counter =0
                    for row in dataTable[i]:
                        try:
                            test = float(row)
                            row="NULL"
                            dataTable[i][counter]=row
                        except ValueError:
                            False
                        counter+=1
                else:
                    counter =0
                    for row in dataTable[i]:
                        try:
                            test=float(row)
                        except:
                            avarage=intTotal/intCounter
                            dataTable[i][counter]=float(int(avarage))
                        counter+=1
                    if(stringCounter>0):
                        missingCount.append([dataTableFields[i],stringCounter])
            dist= list(set(dataTable[i]))
            if(len(dist)>1):
                most = collections.Counter(dataTable[i]).most_common(1)[0][0]
                if most == "NULL":
                    most = collections.Counter(dataTable[i]).most_common(2)[1][0]
                rowCounter=0
                missingStringCount=0
                for row in dataTable[i]:
                    if row == "NULL":
                        dataTable[i][rowCounter]=most
                        missingStringCount+=1
                    rowCounter+=1
                if(missingStringCount>0):
                    missingCount.append([dataTableFields[i],missingStringCount])
        return missingCount
    @staticmethod
    def PivotingDataTable(datatable,pivotColumns,dataTableFields,globalCounter):
        willBeDelete=[]
        for i in range(0,len(datatable)):
            globalCounter+=1
            control = True # Control For Which Column and Fields Will Delete
            distance = list(set(datatable[i]))
            for dist in distance:
                globalCounter+=1
                pivotRows=[]
                try:
                    temp = float(dist)
                    control=False
                except:
                    for row in datatable[i]:
                        globalCounter+=1
                        if row ==dist:
                            if len(pivotRows)<=0:
                                dataTableFields.append(dist) # Fields Update For Pivoting
                            pivotRows.append(float(1))
                        else:
                            if len(pivotRows)<=0:
                                dataTableFields.append(dist)
                            pivotRows.append(float(0))
                    pivotColumns.append(pivotRows)
            if control:
                willBeDelete.append(i)
        willBeDelete.reverse()
        for i in range(0,len(willBeDelete)):
            globalCounter+=1
            del datatable[willBeDelete[i]]
            del dataTableFields[willBeDelete[i]]
    @staticmethod
    def SumClassesCluster(cluster):
        return [sum(i) for i in zip(*cluster)]
    @staticmethod
    def ResetClasterIndex(cluster,count,globalCounter):
        for i in range(count):
            globalCounter+=1
            cluster[i]=[]
    @staticmethod
    def GetEuclid(val1,val2):
        return math.pow(val1-val2,2)
    @staticmethod
    def CopyTo(cluster):
        cls=[]
        for c in cluster:
            cls.append(c)
        return cls
    @staticmethod
    def CompareArray(array1,array2):
        for i in range(0,len(array1)):
            set1=set(array1[i])
            set2=set(array2[i])
            durum =set1.intersection(set2)
            if(len(durum)!=len(array2[i]) or len(durum)!=len(array1[i])):
                return 1
        return 0
    @staticmethod
    def GetAvarage(data):
        if(len(data)>1):
            return [round(sum(i)/len(data),2) for i in zip(*data)]
        else:
            return [sum(i) for i in zip(*data)]
    @staticmethod
    def PassPivotColumnsToDataTable(pivotColumns,dataTable,globalCounter):
        for row in pivotColumns:
            globalCounter+=1
            dataTable.append(row)