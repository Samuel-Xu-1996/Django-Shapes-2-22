from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Sales
from .resources import SalesResource

class SalesAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = SalesResource
    list_display = ('Customerno',
                'CompanyName',
                'DieNumber',
                'Invoiceno',
                'Salesorderno',
                'LinenoAlt',
                'Partno',
                'Partdescr',
                'Dateshipped',
                'Invoicedate',
                'QtyShipped',
                'CalcActualWgt',
                'CalcTheorWgt',
                'CalcPrice',
                'ExtrusionRevenue',
                'PriceperLb',
                'FabricationLbs',
                'FabricationRevenue',
                'PaintLbs',
                'PaintRevenue',
                'AnodizingSqFt',
                'AnodizingRevenue',
                'IngotPrice',
                'Press',
                'Ordertype',
                'Unitofmeas',
                'Productline',
                'Shiptono',
                'ShiptoState',
                'RSM',
                'RSMName'
                  )
    list_per_page = 50


admin.site.register(Sales, SalesAdmin)
