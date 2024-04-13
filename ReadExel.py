import xlrd

class Exel:

    def __init__(self,loc):

        wb = xlrd.open_workbook(loc)
        self.sheet = wb.sheet_by_index(0)

    def extractLine(self,line, start, end):

        newList = []
        for i in range(start, end):
            newList.append(self.sheet.cell_value(line, i))
        return newList

    def extractColom(self,colom,start,end):

        newList = []
        for i in range(start, end):
            newList.append(self.sheet.cell_value(i, colom))
        return newList