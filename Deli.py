# Deli is Class Function.
class Deli:
   

    #Private member variable

    __inputString = ""
    __delimeter = ""

    #Public Properties
    def setInputString(self,value):
        self.__inputString = value

    def setDelimeter(self,value):
        self.__delimeter = value

    def DeliDataRow(self):
        DataRowList = self.__inputString.split(self.__delimeter)

        for i in DataRowList:
            print(i)

