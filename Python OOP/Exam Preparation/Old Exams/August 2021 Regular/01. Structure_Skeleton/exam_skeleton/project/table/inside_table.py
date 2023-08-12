from project.table.table import Table


class InsideTable(Table):

    def type(self):
        return self.__class__.__name__