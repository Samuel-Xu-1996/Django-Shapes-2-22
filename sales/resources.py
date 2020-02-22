from import_export import resources
from .models import Sales

class SalesResource(resources.ModelResource):

    class Meta:
        model = Sales
        fields = ('Customerno',
                'CompanyName',
                'Die_Number',
                'Invoiceno',
                'Salesorderno',
                'Lineno_Alt',
                'Partno',
                'Partdescr',
                'Dateshipped',
                'Invoicedate',
                'Qty_Shipped',
                'Calc_Actual_Wgt',
                'Calc_Theor_Wgt',
                'Calc_Price',
                'Extrusion_Revenue',
                'Price_per_Lb',
                'Fabrication_Lbs',
                'Fabrication_Revenue',
                'Paint_Lbs',
                'Paint_Revenue',
                'Anodizing_Sq_Ft',
                'Anodizing_Revenue',
                'Ingot_Price',
                'Press',
                'Ordertype',
                'Unitofmeas',
                'Productline',
                'Shiptono',
                'Ship_to_State',
                'RSM',
                'RSM_Name'
                  )
