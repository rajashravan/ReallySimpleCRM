from django.http import HttpResponse
from openpyxl import Workbook


def export_to_excel():

    # each item is a line in the excel sheet
    # it can be anything you pull from the db
    excel_data = [
      ['header1', 'header2', 'header3', 'header4', 'header5']
      [1,4,5,6,7],
      [5,6,2,4,8]
    ]

    if excel_data:
        wb = Workbook(write_only=True)
        ws = wb.create_sheet()
        for line in excel_data:
            ws.append(line)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'

    wb.save(response)

    return response
