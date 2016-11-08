# Name: Blake Braun
# Email: bbraun5@slu.edu
# Current Date: 03/25/15
# Course Information: CSCI150-02
# Instructor: Judy Etchison
# Honor Code Statement: In keeping with the honor code policies of Saint Louis
# University, the Department of Mathematics and Computer Science, I affirm that
# I have neither given nor received assistance on this programming assignment.
# This assignment represents my individual, original effort.
class Stock(): 
    def __init__(self, date='01/01/01', opening=0, high=0, low=0, closing=0, vol=0): # Initializes Stock object with default parameters
        self._date = date
        self._openVal = opening
        self._highVal = high
        self._lowVal = low
        self._closeVal = closing
        self._volume = vol
    def setDate(self, date): # Sets stock date
        self._date = date
    def getDate(self): # Gets stock date
        return self._date
    def setOpen(self, val): # Sets stock opening value
        self._openVal = val
    def getOpen(self): # Gets stock opening value
        return self._openVal
    def setHigh(self, val): # Sets stock high value
        self._highVal = val
    def getHigh(self): # Gets stock high value
        return self._highVal
    def setLow(self, val): # Sets stock low value
        self._lowVal = val
    def getLow(self): # Gets stock low value
        return self._lowVal
    def setClose(self, val): # Sets stock closing value
        self._closeVal = val
    def getClose(self): # Gets stock closing value
        return self._closeVal
    def setVolume(self, val): # Sets stock volume
        self._volume = val
    def getVolume(self): # Gets stock volume
        return self._volume
    def __str__(self): # Prints information in Stock object
        return 'Date: ' + self._date + "\n Opening:" + str(self._openVal) + '\n High:' + str(self._highVal) + '\n Low: ' + str(self._lowVal) + '\n Closing:' + str(self._closeVal) + '\n Volume:' + str(self._volume)

    
        
