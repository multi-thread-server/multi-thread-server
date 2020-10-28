import xlrd
import os 

def main():
    file = "student_info.xlsx"
    id = input("Pleas enter id:")

    workbook = xlrd.open_workbook(file)
    Table = workbook.sheet_by_name("Sheet1")
    #Table = workbook.sheet_by_index(0)

    length = Table.nrows
    for i in range(length):
        row = Table.row_values(i)
        if id in row[0]:
         print(row[0:6])