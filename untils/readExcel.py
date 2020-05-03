import xlrd

def readExcels():
    rows = []
    book = xlrd.open_workbook(r'D:\Python\UI\data\fanyi_data.xlsx', 'r')
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        rows.append(sheet.row_values(row, 0, sheet.ncols))
    return rows


