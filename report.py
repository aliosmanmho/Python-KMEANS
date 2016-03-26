__author__ = 'AliOsman & Emrullah'
# coding=utf-8
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
class Report:
    @staticmethod
    def ReportDataToExel(mainData,mainFields,clusters,deletedDistanceColums,deletedSameDataColumn,missingValues,dataTableFields):
        workbook = xlsxwriter.Workbook('Report.xlsx',)
        bold = workbook.add_format({'bold': 1})
        for i in range(0,len(clusters)):
            groupName="Group"+str(i+1)
            worksheet = workbook.add_worksheet(groupName)

            for k in range(0,len(mainFields)):
                worksheet.write(0,k,mainFields[k])
                counter2=1
                for j in range(0,len(clusters[i])):
                    worksheet.write(counter2,k,mainData[k][clusters[i][j]])
                    counter2+=1

        worksheet = workbook.add_worksheet("Report")
        Report.DistanceWrite(worksheet,deletedDistanceColums,bold)
        Report.SameDataWrite(worksheet,deletedSameDataColumn,bold)
        Report.TotalAndMissingeWrite(missingValues,len(mainData[0]),worksheet,bold)
        workbook.close()
    @staticmethod
    def PrintReportScreen(clusterNumber,data,selectedFile,missingeValues):
        n_groups =clusterNumber
        groups=[]
        for row in data:
            groups.append((len(row)))
        n_numberGroups=np.array(groups)
        # The slices will be ordered and plotted counter-clockwise.
        labels =[]
        fig = plt.figure()
        ss = selectedFile.split('/')
        fig.suptitle(ss[len(ss)-1])
        fig.subplots_adjust(bottom=0.15)
        fig.subplots_adjust(left=0.45)
        fig.canvas.set_window_title('K-Means')
        total=0
        for i in range(0,int(clusterNumber)):
            groupName="Group_"+str(i+1)+"\nValues :"+str(len(data[i]))
            labels.append(groupName)
            total+=len(data[i])
        sizes = n_numberGroups
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        #explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

        plt.pie(sizes, labels=labels,colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)

        missingeTotal=0
        for rw in missingeValues:
            missingeTotal+=rw[1]
        plt.text(-3, 1, 'Total Values : '+str(total)+"\n"+"Missinge Values : "+str(missingeTotal), style='italic')
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.show()
        plt.close(),
    @staticmethod
    def DistanceWrite(worksheet,deletedDistanceColums,bold):
        worksheet.write_column('A1',["Distance Deleted Columns"],bold)
        worksheet.write_column('B1',["Column Name"],bold)
        worksheet.write_column('C1',["Value"],bold)
        for i in range(0,len(deletedDistanceColums)):
            worksheet.write(i+1,1,deletedDistanceColums[i][1])
            worksheet.write(i+1,2,str(deletedDistanceColums[i][2]))
    @staticmethod
    def SameDataWrite(worksheet,deletedSameDataColumn,bold):
        worksheet.write_column('E1',["SameData Deleted Columns"],bold)
        worksheet.write_column('F1',["Name"],bold)
        worksheet.write_column('G1',["Count"],bold)
        worksheet.write_column('H1',["Value"],bold)
        for i in range(0,len(deletedSameDataColumn)):
            worksheet.write(i+1,5,str(deletedSameDataColumn[i][0]))
            worksheet.write(i+1,6,str(deletedSameDataColumn[i][1]))
            worksheet.write(i+1,7,str(deletedSameDataColumn[i][2]))
    @staticmethod
    def TotalAndMissingeWrite(missingValues,total,worksheet,bold):
        worksheet.write_column('J1',["Missing Values"],bold)
        worksheet.write_column('K1',["Column Name"],bold)
        worksheet.write_column('L1',["Count"],bold)
        for i in range(0,len(missingValues)):
            worksheet.write(i+1,10,str(missingValues[i][0]))
            worksheet.write(i+1,11,str(missingValues[i][1]))
        worksheet.write_column('N1',["Total Value"],bold)
        worksheet.write(1,13,str(total))


