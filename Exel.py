import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.load_workbook("123.xlsx")

sheet = wb.active



sheet.merge_cells('A1:A2')
sheet.merge_cells('B1:B2')
sheet.merge_cells('C1:C2')
sheet.merge_cells('D1:D2')
sheet.merge_cells('E1:F1')
sheet.merge_cells('G1:H1')
sheet.merge_cells('I1:I2')
sheet.merge_cells('J1:J2')
sheet.merge_cells('K1:K2')
sheet.cell(row=1, column=1).value = '№ п/п'
sheet.cell(row=1, column=1).alignment = Alignment(textRotation=90)
sheet.cell(row=1, column=2).value = 'Команда'
sheet.cell(row=1, column=3).value = 'Фамилия, имя'
sheet.cell(row=1, column=4).value = '№ нагрудный'
sheet.cell(row=1, column=4).alignment = Alignment(textRotation=90)
sheet.cell(row=1, column=5).value = 'Стрельба'
sheet.cell(row=2, column=5).value = 'Результат'
sheet.cell(row=2, column=5).alignment = Alignment(textRotation=90)
sheet.cell(row=2, column=6).value = 'Очки'
sheet.cell(row=2, column=6).alignment = Alignment(textRotation=90)
sheet.cell(row=1, column=7).value = 'Бег'
sheet.cell(row=2, column=7).value = 'Результат'
sheet.cell(row=2, column=7).alignment = Alignment(textRotation=90)
sheet.cell(row=2, column=8).value = 'Очки'
sheet.cell(row=2, column=8).alignment = Alignment(textRotation=90)
sheet.cell(row=1, column=9).value = 'Сумма двоеборья'
sheet.cell(row=1, column=10).value = 'Личное место'
sheet.cell(row=1, column=11).value = 'Сумма 4-х лучших личных мест'
sheet.column_dimensions['A'].width = 5
sheet.column_dimensions['B'].width = 15
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['I'].width = 15
sheet.column_dimensions['K'].width = 15
sheet.row_dimensions[2].height = 75
count_of_teams = 3
id_team = 1
for x in range(3,  count_of_teams * 5):
    sheet.cell(row = x, column=1).value = x - 2
    if x % 10 == 3:
        sheet.merge_cells(f'B{x}:B{x + 10}')
        sheet.cell(row=x, column=2).value = id_team
        id_team+=1


for col in sheet.columns:
    for cell in col:
        # openpyxl styles aren't mutable,
        # so you have to create a copy of the style, modify the copy, then set it back
        alignment_obj = cell.alignment.copy(horizontal='center', vertical='center', wrap_text=True)
        cell.alignment = alignment_obj

wb.save('123.xlsx')