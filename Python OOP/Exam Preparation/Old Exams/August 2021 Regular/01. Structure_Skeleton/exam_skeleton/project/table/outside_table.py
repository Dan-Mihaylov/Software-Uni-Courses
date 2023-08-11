from project.table.table import Table


class OutsideTable(Table):

    def type(self):
        return self.__class__.__name__