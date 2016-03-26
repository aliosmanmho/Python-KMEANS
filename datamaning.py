#!/Python27/python.exe
# coding=utf-8


__author__ = 'AliOsman & Emrullah'
import csv

from  functions import *
from  report import *
import threading
import multiprocessing
import math
import collections

from KMEANS import KMEANS

class DataMiningProject:
    @staticmethod
    def Run(self,selectedDB,clusterNumber,clicked):

        globalCounter=0
        kmeansCounter=1
        mainDataTableFields=""
        dataTableFields=[]
        pivotColumns =[]
        missingValues=[]
        deletedDistanceColums=[]
        deletedSameDataColumn=[]
        mainDataTable = []
        dataTable=[]
        tempList = []
        from time import gmtime, strftime
        print "Started Time"
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print "\n"
        ColumCount=0
        with open(selectedDB, 'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=';')
            mainDataTableFields = reader.next()
            ColumCount = next(reader)
            counter=0
            for row in reader:
                globalCounter+=1
                lst = []
                for rw in row:
                    globalCounter+=1
                    try:
                        temp = float(rw)
                        lst.append(float(temp))
                    except:
                        lst.append(rw)
                tempList.append(lst)



        functions.MainFieldsToFields(mainDataTableFields,dataTableFields,globalCounter)
        functions.FillMainDataTable(mainDataTable,tempList,len(ColumCount),globalCounter)
        deletedDistanceColums=functions.DistanceDataTable(mainDataTable,dataTable,dataTableFields,globalCounter)
        deletedSameDataColumn=functions.SameDataDelete(dataTable,dataTableFields,globalCounter)
        missingValues=functions.FillMissingValues(dataTable,globalCounter,dataTableFields)
        functions.PivotingDataTable(dataTable,pivotColumns,dataTableFields,globalCounter)
        functions.PassPivotColumnsToDataTable(pivotColumns,dataTable,globalCounter)

        data = list(zip(*dataTable)) # DataTable inversely
        if (clicked=="Kmeans"):
            d=KMEANS.KMeans(data,int(clusterNumber),globalCounter)
        else:
            d=KMEANS.KMeansPer(data,int(clusterNumber),globalCounter)

        print kmeansCounter
        print "Finished Time"
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print d[3]
        Report.ReportDataToExel(mainDataTable,mainDataTableFields,d[1],deletedDistanceColums,deletedSameDataColumn,missingValues,dataTableFields)




        Report.PrintReportScreen(clusterNumber,d[1],selectedDB,missingValues)




