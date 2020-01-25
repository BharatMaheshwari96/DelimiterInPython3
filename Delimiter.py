from Deli import Deli

parses = Deli()

DataRow = input("Enter your data row:")
Delimeter = input("Enter your delimeter:")

parses.setInputString(DataRow)
parses.setDelimeter(Delimeter)

parses.DeliDataRow()
