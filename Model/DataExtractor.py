
class DataExtractor:
    def __init__(self):
        self.dataDict = {}

    def resetDataDict(self):
        self.dataDict = {}

    def addData(self, path, dataName, splitSymbol, deleteFirstRow=0, xValuesPos=0, yValuesPos=1):
        """Add data in the dictionnary.
        Args:
            path(str): The path of the file.
            dataName(str): The key to add in the dictionnary.
            splitSymbol(str): The split symbol between each data.
            [Facultative]
            deleteFirstRow(int): The number of row you want to avoid at the start of the file.
            xValuesPos(int): The column of x values.
            yValuesPos(int): The column of y values.
        Return:
            None
        """
        fich = open(path, "r")
        fich_str = list(fich)[deleteFirstRow:]
        fich.close()
        x = []
        y = []
        for i in fich_str:
            elem_str = i.replace("\n", "")
            elem = elem_str.split(splitSymbol)
            x.append(float(elem[xValuesPos]))
            y.append(float(elem[yValuesPos]))
        self.dataDict[dataName] = {"xValues": x, "yValues": y}

    def deleteData(self, dataName):
    	self.dataDict.pop(dataName)

    def getData(self, dataName):
        data = self.dataDict.get(dataName)
        return data
