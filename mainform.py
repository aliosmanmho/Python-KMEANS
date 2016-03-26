__author__ = 'AliOsman & Emrullah'
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import *
from tkFileDialog import askopenfilename

from datamaning import *

class MainForm(Tkinter.Frame):
    selectedFile =""
    def __init__(self, master):
        frame= Frame(master)
        frame.pack()
        self.theLabel = Label(frame, text="Please enter cluster number: ", bg="orange")
        self.theLabel.pack(side=LEFT)
        self.entryClusterNumber = Entry(frame, bg="red")
        self.entryClusterNumber.pack(side=LEFT)

        self.emptyLabel = Label(frame, text="ll")
        self.emptyLabel.pack(side=LEFT)

        self.Quit = Button(frame,text="Quit",fg="white", bg="black", command=self.Close)
        self.Quit.pack(side=RIGHT)


        #self.button1 = Button(frame, text="Enter", fg="red",command=self.SetClusterNumber)
        self.button1 = Button(frame, text="...", fg="red",width="10",command=self.SelectFile)
        self.button1.pack(side = LEFT)

        #self.selectFile=Button(frame,text="askopenfile", command=self.SelectFile)
        #self.selectFile.pack(side=LEFT)

        self.kmeans = Button(frame,text="Run K-Means",command=self.kmeans)
        self.kmeans.pack(side=LEFT)

        self.kmeans2 = Button(frame,text="Run K-Means with 30 percent",command=self.kmeansper)
        self.kmeans2.pack(side=LEFT)


        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
        options['initialdir'] = 'C:\\Users\\Emrullah\\Documents'
        options['initialfile'] = 'file.csv'
        options['parent'] = root
        options['title'] = 'Select file'

        # *** Status Bar ***
        self.status = Label(root,text="The application is goint to start, Do nothing...", bd=1, relief=SUNKEN, anchor=W)


# bu normal k means
    def kmeans(self):
        DataMiningProject.Run(self,self.selectedFile,self.SetClusterNumber(),"Kmeans")
        self.ShwSttsBar()

    def kmeansper(self):
        DataMiningProject.Run(self,self.selectedFile,self.SetClusterNumber(),"KMeansPer")
        self.ShwSttsBar()

    def ShwSttsBar(self):
        self.status.pack(side=BOTTOM, fill=X)

    def SetClusterNumber(self):
        print("setted")
        print self.entryClusterNumber.get()
        return self.entryClusterNumber.get()
        self.ShwSttsBar()

    def SelectFile(self):
        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        print(filename)
        self.selectedFile=filename
        return filename

    def Close(self):
        root.quit()


root = Tk()
root.wm_title("Clustering With K-Means Algorithm")
form = MainForm(root)
topFrame = Frame(root, width=300, height=15)
topFrame.pack()
root.mainloop()
