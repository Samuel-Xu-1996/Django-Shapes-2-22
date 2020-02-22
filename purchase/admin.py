from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Purchase
from .resources import PurchaseResource

class PurchaseAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = PurchaseResource
    list_display = ('PO',
                  'VendorNo',
                  'VendorName',
                  'Line',
                  'Partno',
                  'Partdescr',
                  'GLAccountno',
                  'Datepromised',
                  'Qtyonorder',
                  'Price',
                  'LineAmount',
                  'Requestedby',
                  'Buyer',
                  'Status',
                  'Projectno',
                  'ProjectDesc'
                  )
    list_per_page = 50


admin.site.register(Purchase, PurchaseAdmin)
