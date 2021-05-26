import xlsxwriter


workbook = xlsxwriter.Workbook("expenses02.xlsx")
worksheet = workbook.add_worksheet("May")

expenses = (
    ["rent", 2000],
    ["food", 1000],
    ["commute", 800],
    ["treats", 200],
)

row = 0
col = 0

for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)

# worksheet.write(row, 0, "Total")
# worksheet.write(row, 1, "=sum(B1:B4)")

workbook.close()