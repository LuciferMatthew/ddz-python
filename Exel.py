import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment

#wb = openpyxl.load_workbook("exel.xlsx")
wb = Workbook()
#sheet = wb.active
sheet = wb.active



sheet.merge_cells('A3:A4')
sheet.merge_cells('B3:B4')
sheet.merge_cells('C3:C4')
sheet.merge_cells('D3:D4')
sheet.merge_cells('E3:F3')
sheet.merge_cells('G3:H3')
sheet.merge_cells('I3:I4')
sheet.merge_cells('J3:J4')
sheet.merge_cells('K3:K4')
sheet.cell(row=3, column=1).value = '№ п/п'
sheet.cell(row=3, column=1).alignment = Alignment(textRotation=90)
sheet.cell(row=3, column=2).value = 'Команда'
sheet.cell(row=3, column=3).value = 'Фамилия, имя'
sheet.cell(row=3, column=4).value = '№ нагрудный'
sheet.cell(row=3, column=4).alignment = Alignment(textRotation=90)
sheet.cell(row=3, column=5).value = 'Стрельба'
sheet.cell(row=4, column=5).value = 'Результат'
sheet.cell(row=4, column=5).alignment = Alignment(textRotation=90)
sheet.cell(row=4, column=6).value = 'Очки'
sheet.cell(row=4, column=6).alignment = Alignment(textRotation=90)
sheet.cell(row=3, column=7).value = 'Бег'
sheet.cell(row=4, column=7).value = 'Результат'
sheet.cell(row=4, column=7).alignment = Alignment(textRotation=90)
sheet.cell(row=4, column=8).value = 'Очки'
sheet.cell(row=4, column=8).alignment = Alignment(textRotation=90)
sheet.cell(row=3, column=9).value = 'Сумма двоеборья'
sheet.cell(row=3, column=10).value = 'Личное место'
sheet.cell(row=3, column=11).value = 'Сумма 4-х лучших личных мест'
sheet.column_dimensions['A'].width = 5
sheet.column_dimensions['B'].width = 15
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['I'].width = 15
sheet.column_dimensions['K'].width = 15
sheet.row_dimensions[4].height = 75
count_of_teams = 3
id_team = 1
max_values = [] * 4
for x in range(5,  count_of_teams * 10 + 5):
    sheet.cell(row = x, column=1).value = x - 4

    if x % 10 == 5:
        sheet.cell(row=x, column=11).value = f"=SUM(LARGE(L{x}:L{x+9},{{1,2,3,4}}))"
        max_values = [] * 4
        sheet.merge_cells(f'B{x}:B{x + 9}')
        sheet.cell(row=x, column=2).value = id_team
        sheet.merge_cells(f'I{x}:I{x + 9}')
        sheet.merge_cells(f'K{x}:K{x + 9}')
        sheet.cell(row=x, column=9).value = f"=SUM(F{x}:F{x + 9}) + SUM(H{x}:H{x + 9})"
        id_team+=1




for col in sheet.columns:
    for cell in col:
        # openpyxl styles aren't mutable,
        # so you have to create a copy of the style, modify the copy, then set it back
        alignment_obj = cell.alignment.copy(horizontal='center', vertical='center', wrap_text=True)
        cell.alignment = alignment_obj

wb.save('Mysheet.xlsx')