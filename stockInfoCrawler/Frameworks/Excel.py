__author__ = 'Ryan'

from xlrd import open_workbook


class Excel(object):
    __file_name = ""
    __book = None
    __sheet = None

    def __init__(self):
        pass

    def open_book(self, file_name):
        self.__file_name = file_name
        self.__book = open_workbook(file_name)

    def open_sheet_by_name(self, sheet_name):
        self.__sheet = self.__book.sheet_by_name(sheet_name)

    def open_sheet_by_index(self, sheet_index):
        self.__sheet = self.__book.sheet_by_index(sheet_index)

    def read_cell(self, row, col):
        return self.__sheet.cell(row, col).value

    def read_block(self, begin_row, end_row, begin_col, end_col):
        if begin_row >= end_row:
            print "The number of row is wrong, from %d to %d" % (begin_row, end_row)
            return None
        if begin_col >= end_col:
            print "The number of col is wrong, from %d to %d" % (begin_col, end_col)
            return None
        data = []
        for row in range(begin_row, end_row):
            data_row = []
            for col in range(begin_col, end_col):
                data_row.append(self.__sheet.cell(row, col).value)
            data.append(data_row)
        return data

    def read_cols(self, begin_row, end_row, cols):
        if begin_row >= end_row:
            print "The number of row is wrong, from %d to %d" % (begin_row, end_row)
            return None
        data = []
        for row in range(begin_row, end_row):
            data_row = []
            for col in cols:
                data_row.append(self.__sheet.cell(row, col).value)
            data.append(data_row)
        return data