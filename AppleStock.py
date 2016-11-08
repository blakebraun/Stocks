# Name: Blake Braun
# Email: bbraun5@slu.edu
# Current Date: 03/25/15
# Course Information: CSCI150-02
# Instructor: Judy Etchison
# Honor Code Statement: In keeping with the honor code policies of Saint Louis
# University, the Department of Mathematics and Computer Science, I affirm that
# I have neither given nor received assistance on this programming assignment.
# This assignment represents my individual, original effort.
from StockClass import *
class AppleStock():
    def __init__(self, fileObj = None, stockObj = []): # Initializes AppleStock object with default parameters
        self._fileObj = fileObj
        self._stockObj = stockObj
    def openFile(self): # Validates filename and opens file
        while not self._fileObj:
            fileName = raw_input('Open what file? ')
            try:
                self._fileObj = file(fileName)
            except IOError:
                print 'Bad file name, try again.'
    def get_data_list(self): # Opens file using openFile method, reads in source, and creates new Stock objects from each line of source, adding each to a list. Removes first line from list.
        self.openFile()
        line = self._fileObj.readline()
        while line:
            data = line.split('\t')
            stock = Stock(data[0], data[1], data[2], data[3], data[4], data[5])
            self._stockObj.append(stock)
            line = self._fileObj.readline()
        self._stockObj.pop(0)
        self._fileObj.close()
    def getMonth(self, num): # Translates number of month to the name in the average_data method
        num = int(num)
        if num == 1:
            return 'January'
        elif num == 2:
            return 'February'
        elif num == 3:
            return 'March'
        elif num == 4:
            return 'April'
        elif num == 5:
            return 'May'
        elif num == 6:
            return 'June'
        elif num == 7:
            return 'July'
        elif num == 8:
            return 'August'
        elif num == 9:
            return 'September'
        elif num == 10:
            return 'October'
        elif num == 11:
            return 'November'
        elif num == 12:
            return 'December'
        else:
            return 'n/a'
    def average_data(self): # Validates year input, finds the year in the source, finds the highest opening value and lowest closing value by comparing them to each other, calculates averages, and prints them.
        validYear = False
        openMonth = ''
        closeMonth = ''
        entries = 0
        highOpen = 0
        lowClose = 1000
        openVal = 0
        closeVal = 0
        highVal = 0
        lowVal = 0
        volume = 0
        userYear = raw_input("What year do you want averaged?")
        while not validYear:
            if len(userYear) == 4 and userYear.isdigit() == True and int(userYear) >= 1984 and int(userYear) <= 2013:
                validYear = True
            else:
                userYear = raw_input('Invalid year. Reenter year: ')
                validYear = False
        for i in range(len(self._stockObj)):
            date = self._stockObj[i].getDate().split('/')
            if date[2] == userYear:
                entries += 1
                if float(self._stockObj[i].getOpen()) >= highOpen:
                    openMonth = date[0]
                    highOpen = float(self._stockObj[i].getOpen())
                if float(self._stockObj[i].getClose()) <= lowClose:
                    closeMonth = date[0]
                    lowClose = float(self._stockObj[i].getClose())
                openVal += float(self._stockObj[i].getOpen())
                closeVal += float(self._stockObj[i].getClose())
                highVal += float(self._stockObj[i].getHigh())
                lowVal += float(self._stockObj[i].getLow())
                volume += float(self._stockObj[i].getVolume())
        openVal = int(openVal/entries)
        closeVal = int(closeVal/entries)
        highVal = int(highVal/entries)
        lowVal = int(lowVal/entries)
        volume = int(volume/entries)
        print "Here are the averages for Apple Stock for year " + userYear + "\n" + "Opening\tClosing\tHigh\tLow\tClose\tVolume\n" + str(openVal) + "\t" + str(closeVal) + "\t" + str(highVal) + "\t" + str(lowVal) + "\t" + str(closeVal) + "\t"+ str(volume) + "\n" + "The month with the highest opening value was " + self.getMonth(openMonth) + " with " + str(highOpen) + "\n" + "The month with the lowerst closing value was " + self.getMonth(closeMonth) + " with " + str(lowClose) + "\n"                                  
