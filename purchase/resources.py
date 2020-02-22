from import_export import resources
from .models import Purchase

class PurchaseResource(resources.ModelResource):

    class Meta:
        model = Purchase
        fields = ('PO',
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
