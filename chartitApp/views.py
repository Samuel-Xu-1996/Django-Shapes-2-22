from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesReport, MonthlyWeatherByCity, SalesCompany, PurchaseCode, PurchaseReport, InventoryReport, MonthlyRevenue,\
     OrderRep, OrderCustomer, OrderDate, OrderBl, OrderCl, OrderDa, OrderS1, OrderS2, OrderS3, OrderS4,\
     OveralloneDep, OveralltwoDep, OverallthreeDep,\
     PivotBudget, FoundryoneMonth, FoundrytwoMonth, FoundrythreeMonth, FoundryallMonth, FoundrycompareMonth,\
     FoundryoneVendor, FoundrytwoVendor, FoundrythreeVendor,\
     FoundryoneItem, FoundrytwoItem, FoundrythreeItem,\
     FoundryoneExpense, FoundrytwoExpense, FoundrythreeExpense,\
     FoundryonetopItem, FoundrytwotopItem, FoundrythreetopItem,\
     FoundrycompareScrap, FoundrycomparePrime, FoundrycompareLog,\
     FoundrymainCompare, FoundrymainMini, FoundrymainAll,\
     ExtrusiononeItem, ExtrusiontwoItem, ExtrusionthreeItem,\
     ExtrusiononetopItem, ExtrusiontwotopItem, ExtrusionthreetopItem,\
     ExtrusiononeMonth, ExtrusiontwoMonth, ExtrusionthreeMonth, ExtrusionallMonth, ExtrusioncompareMonth,\
     ExtrusioncompareMain,\
     SalesoneRep, SalestwoRep, SalesthreeRep,\
     SalesoneCustomer, SalestwoCustomer, SalesthreeCustomer,\
     SalesoneMonth, SalestwoMonth, SalesthreeMonth, SalesallMonth,\
     SalesoneBl, SalestwoBl, SalesthreeBl, SalesallBl, SalescompareBl,\
     SalesoneCl, SalestwoCl, SalesthreeCl, SalesallCl, SalescompareCl,\
     SalesoneDa, SalestwoDa, SalesthreeDa, SalesallDa, SalescompareDa,\
     SalesoneS1, SalestwoS1, SalesthreeS1, SalesallS1, SalescompareS1,\
     SalesoneS2, SalestwoS2, SalesthreeS2, SalesallS2, SalescompareS2,\
     SalesoneS3, SalestwoS3, SalesthreeS3, SalesallS3, SalescompareS3,\
     SalesoneS4, SalestwoS4, SalesthreeS4, SalesallS4, SalescompareS4,\
     SalesoneDep, SalestwoDep, SalesthreeDep, SalesallDep,\
     SalesextrusionDep, SalesfabricationDep, SalesanodizingDep
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def notification(request):
    return render(request, 'notification.html')

def openorder(request):
    return render(request,'openorder.html')

def budgetReport(request):
    return render(request,'budgetreport.html')

def sales(request):
    sales =  DataPool(
           series=
            [{'options': {
            #    'source': SalesReport.objects.all()},
            'source': SalesReport},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'month': 'month',
                'sales': 'sales'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'sales']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Monthly Sales'},
               'xAxis': {
                   'title':{'text': 'Month Number'}},
               'yAxis': {
                   'title': {'text': 'Sales Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'sales']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Monthly Sales - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def salesCompany(request):
    sales =  DataPool(
           series=
            [{'options': {
            'source': SalesCompany.objects.all()},
                'terms': [{'customer': 'customer',
                'sales': 'sales'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'customer': [
                    'sales']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Sales Amounts For Each Customer'},
               'xAxis': {
                   'title':{'text': 'Customer'}},
               'yAxis': {
                   'title': {'text': 'Sales Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'customer': [
                    'sales']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Sales Amounts For Each Customer - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Customer'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})



def purchase(request):
    purchase =  DataPool(
           series=
            [{'options': {

            'source': PurchaseReport},
                'terms': [{'month': 'month',
                'purchase': 'purchase'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = purchase,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'purchase']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Monthly Purchase'},
               'xAxis': {
                   'title':{'text': 'Month Number'}},
               'yAxis': {
                   'title': {'text': 'Purchase Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = purchase,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'purchase']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Monthly Purchase - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Purchase Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def purchaseCode(request):
    purchase =  DataPool(
           series=
            [{'options': {
            'source': PurchaseCode.objects.all()},
                'terms': [{'department': 'department',
                'purchase': 'purchase'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = purchase,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'department': [
                    'purchase']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Purchase Amounts For Each Department'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Purchase Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = purchase,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'department': [
                    'purchase']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Purchase Amounts For Each Department - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Purchase Total'}},
               'yAxis': {
                   'title': {'text': 'Department'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'WABASH_sales',
                'UHAUL_sales']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'WABASH_sales',
                'UHAUL_sales']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Monthly Sales Data of UHAUL and WABASH'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render(request,'weatherchart.html', {'weatherchart': cht})    


def weatherByCity(request):
    ds = DataPool(
        series=[{
            'options': {
                'source': MonthlyWeatherByCity.objects.all()
            },
            'terms': [
                'month',
                'WABASH_sales',
                'WABASH'
            ]
        }]
)
    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov',
             12: "Dec"}
        return names[month_num]

    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'line'
            },
            'terms': {
                'month': ['WABASH']
            }}, {
            'options': {
                'type': 'pie',
                'center': [750, 70],
                'size': '50%'
            },
            'terms': {
                'month': ['WABASH_sales']
            }}
        ],
        chart_options={
            'title': {
                'text': 'Monthly Sales Data of WABASH'
            }
        },
        x_sortf_mapf_mts=[(None, monthname, False),
                          (None, monthname, False)])   

    return render(request,'weatherByCity.html', {'weatherByCity': cht})

def inventory(request):
    inventory =  DataPool(
           series=
            [{'options': {

            'source': InventoryReport},
                'terms': [{'month': 'month',
                'inventory': 'inventory'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = inventory,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'inventory']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Monthly Inventory'},
               'xAxis': {
                   'title':{'text': 'Month Number'}},
               'yAxis': {
                   'title': {'text': 'Inventory Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = inventory,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'inventory']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Monthly Inventory - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Inventory Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def revenue(request):
    revenue =  DataPool(
           series=
            [{'options': {

            'source': MonthlyRevenue},

                'terms': [{'month': 'month',
                'revenue': 'revenue'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = revenue,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'revenue']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Monthly revenue'},
               'xAxis': {
                   'title':{'text': 'Month Number'}},
               'yAxis': {
                   'title': {'text': 'Revenue Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = revenue,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'revenue']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Monthly revenue - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Revenue Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderRep(request):
    orderrep =  DataPool(
           series=
            [{'options': {
            'source': OrderRep.objects.all()},
                'terms': [{'rep': 'rep',
                'weight': 'weight'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orderrep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'rep': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Open Sales Order in LBS of Each Sales Rep'},
               'xAxis': {
                   'title':{'text': 'Sales Representative'}},
               'yAxis': {
                   'title': {'text': 'Weight'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orderrep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'rep': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Open Sales Order in LBS of Each Sales Rep - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Sales Representative'}},
               'yAxis': {
                   'title': {'text': 'Weight'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderCustomer(request):
    ordercustomer =  DataPool(
           series=
            [{'options': {
            'source': OrderCustomer.objects.all()},
                'terms': [{'customer': 'customer',
                'weight': 'weight'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = ordercustomer,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'customer': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Open Sales Order in LBS of Each Customer'},
               'xAxis': {
                   'title':{'text': 'Customer'}},
               'yAxis': {
                   'title': {'text': 'Weight'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = ordercustomer,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'customer': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Open Sales Order in LBS of Each Customer - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'weight'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderDate(request):
    orderdate =  DataPool(
           series=
            [{'options': {

            'source': OrderDate},

                'terms': [{'date': 'date',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020'
            #, 2003: 'Mar 2020', 2004: 'Apr 2020', 2005: 'May 2020', 2006: 'Jun 2020',
            #2007: 'Jul 2020', 2008: 'Aug 2020', 2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orderdate,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'date': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Promised Date of Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'date'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orderdate,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'date': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Promised Date of Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'date'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderBl(request):
    orderbl =  DataPool(
           series=
            [{'options': {

            'source': OrderBl},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orderbl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'BL Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orderbl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'BL Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderCl(request):
    ordercl =  DataPool(
           series=
            [{'options': {

            'source': OrderCl},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = ordercl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'CL Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = ordercl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'CL Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderDa(request):
    orderda =  DataPool(
           series=
            [{'options': {

            'source': OrderDa},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orderda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'DA Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orderda,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'DA Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderS1(request):
    orders1 =  DataPool(
           series=
            [{'options': {

            'source': OrderS1},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orders1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'S1 Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orders1,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'S1 Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderS2(request):
    orders2 =  DataPool(
           series=
            [{'options': {

            'source': OrderS2},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orders2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'S2 Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orders2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'S2 Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderS3(request):
    orders3 =  DataPool(
           series=
            [{'options': {

            'source': OrderS3},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orders3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'S3 Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orders3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'S3 Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def orderS4(request):
    orders4 =  DataPool(
           series=
            [{'options': {

            'source': OrderS4},

                'terms': [{'month': 'month',
                'weight': 'weight'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = orders4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'S4 Open Sales Order in LBS'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = orders4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'S4 Open Sales Order in LBS - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def pivotBudget(request):
    pivotbudget =  DataPool(
           series=
            [{'options': {

            'source': PivotBudget},

                'terms': [{'month': 'month',
                'weight': 'OrderLbs'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
            #1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
            #1907: 'Jul 2019', 1908: 'Aug 2019',
                 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
                 2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = pivotbudget,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'weight']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Monthly Planned Workload'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = pivotbudget,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'weight']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Monthly Planned Workload - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'weight'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def overalloneDep(request):
    overallonedep =  DataPool(
           series=
            [{'options': {
            'source': OveralloneDep.objects.all()},
                'terms': [{'department': 'department',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = overallonedep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'department': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Department Cost'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = overallonedep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'department': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Department Cost - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def overalltwoDep(request):
    overalltwodep =  DataPool(
           series=
            [{'options': {
            'source': OveralltwoDep.objects.all()},
                'terms': [{'department': 'department',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = overalltwodep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'department': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Department Cost'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = overalltwodep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'department': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Department Cost - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def overallthreeDep(request):
    overallthreedep =  DataPool(
           series=
            [{'options': {
            'source': OverallthreeDep.objects.all()},
                'terms': [{'department': 'department',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = overallthreedep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'department': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Department Cost'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = overallthreedep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'department': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Department Cost - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Department'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def foundrymainCompare(request):
    foundrymaincompare =  DataPool(
           series=
            [{'options': {

            'source': FoundrymainCompare},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one',
                '2020': 'zero'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrymaincompare,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019','2020']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2020 Foundry maintenance amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrymaincompare,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019','2020']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2020 Foundry maintenance amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrymainMini(request):
    foundrymainmini =  DataPool(
           series=
            [{'options': {
            'source': FoundrymainMini.objects.all()},
                'terms': [{'year': 'year',
                'cost': 'cost'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrymainmini,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'year': [
                    'cost']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017~2019 Each Year Foundry Maintenance Cost'},
               'xAxis': {
                   'title':{'text': 'Year'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrymainmini,
            series_options =
              [{'options':{
                  'type': 'line',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'year': [
                    'cost']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017~2019 Each Year Foundry Maintenance Cost - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Year'}},
               'yAxis': {
                   'title': {'text': 'Cost Total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrymainAll(request):
    foundrymainall =  DataPool(
           series=
            [{'options': {

            'source': FoundrymainAll},

                'terms': [{'month': 'month',
                'amount': 'cost'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                2001: 'Jan 2020', 2002: 'Feb 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrymainall,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Maintenance cost amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrymainall,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Maintenance cost amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def foundryoneMonth(request):
    foundryonemonth =  DataPool(
           series=
            [{'options': {

            'source': FoundryoneMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryonemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryonemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrytwoMonth(request):
    foundrytwomonth =  DataPool(
           series=
            [{'options': {

            'source': FoundrytwoMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrytwomonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrytwomonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrythreeMonth(request):
    foundrythreemonth =  DataPool(
           series=
            [{'options': {

            'source': FoundrythreeMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrythreemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrythreemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryallMonth(request):
    foundryallmonth =  DataPool(
           series=
            [{'options': {

            'source': FoundryallMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryallmonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryallmonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrycompareMonth(request):
    foundrycomparemonth =  DataPool(
           series=
            [{'options': {

            'source': FoundrycompareMonth},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrycomparemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry purchase amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrycomparemonth,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry purchase amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryoneVendor(request):
    foundryonevendor =  DataPool(
           series=
            [{'options': {
            'source': FoundryoneVendor.objects.all()},
                'terms': [{'vendor': 'vendor',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryonevendor,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each vendor in USD'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryonevendor,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each vendor in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrytwoVendor(request):
    foundrytwovendor =  DataPool(
           series=
            [{'options': {
            'source': FoundrytwoVendor.objects.all()},
                'terms': [{'vendor': 'vendor',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrytwovendor,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each vendor in USD'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrytwovendor,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each vendor in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrythreeVendor(request):
    foundrythreevendor =  DataPool(
           series=
            [{'options': {
            'source': FoundrythreeVendor.objects.all()},
                'terms': [{'vendor': 'vendor',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrythreevendor,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each vendor in USD'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrythreevendor,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each vendor in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryallVendor(request):
    foundryallvendor =  DataPool(
           series=
            [{'options': {
            'source': FoundryallVendor.objects.all()},
                'terms': [{'vendor': 'vendor',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryallvendor,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each vendor in USD'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryallvendor,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'vendor': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each vendor in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'vendor'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryoneItem(request):
    foundryoneitem =  DataPool(
           series=
            [{'options': {
            'source': FoundryoneItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryoneitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryoneitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrytwoItem(request):
    foundrytwoitem =  DataPool(
           series=
            [{'options': {
            'source': FoundrytwoItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrytwoitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrytwoitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrythreeItem(request):
    foundrythreeitem =  DataPool(
           series=
            [{'options': {
            'source': FoundrythreeItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrythreeitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrythreeitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryallItem(request):
    foundryallitem =  DataPool(
           series=
            [{'options': {
            'source': FoundryallItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryallitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryallitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Foundry Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryoneExpense(request):
    foundryoneexpense =  DataPool(
           series=
            [{'options': {
            'source': FoundryoneExpense.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryoneexpense,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Foundry Expense (metal cost excluded) each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryoneexpense,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Foundry Expense (metal cost excluded) each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrytwoExpense(request):
    foundrytwoexpense =  DataPool(
           series=
            [{'options': {
            'source': FoundrytwoExpense.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrytwoexpense,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Foundry Expense (metal cost excluded) each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrytwoexpense,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Foundry Expense (metal cost excluded) each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrythreeExpense(request):
    foundrythreeexpense =  DataPool(
           series=
            [{'options': {
            'source': FoundrythreeExpense.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrythreeexpense,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Foundry Expense (metal cost excluded) each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrythreeexpense,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Foundry Expense (metal cost excluded) each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundryonetopItem(request):
    foundryonetopitem =  DataPool(
           series=
            [{'options': {

            'source': FoundryonetopItem},

                'terms': [{'month': 'month',
                'Aluminum Scrap': 'scrap',
                'Prime Aluminum': 'prime',
                'Log and Billet': 'log'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundryonetopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount for top3 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundryonetopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Foundry Purchase amount for top3 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrytwotopItem(request):
    foundrytwotopitem =  DataPool(
           series=
            [{'options': {

            'source': FoundrytwotopItem},

                'terms': [{'month': 'month',
                'Aluminum Scrap': 'scrap',
                'Prime Aluminum': 'prime',
                'Log and Billet': 'log'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrytwotopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount for top3 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrytwotopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Foundry Purchase amount for top3 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrythreetopItem(request):
    foundrythreetopitem =  DataPool(
           series=
            [{'options': {

            'source': FoundrythreetopItem},

                'terms': [{'month': 'month',
                'Aluminum Scrap': 'scrap',
                'Prime Aluminum': 'prime',
                'Log and Billet': 'log'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrythreetopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount for top3 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrythreetopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Aluminum Scrap','Prime Aluminum','Log and Billet']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Foundry Purchase amount for top3 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrycompareScrap(request):
    foundrycomparescrap =  DataPool(
           series=
            [{'options': {

            'source': FoundrycompareScrap},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrycomparescrap,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Aluminum Scrap Purchase amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrycomparescrap,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Aluminum Scrap Purchase amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrycomparePrime(request):
    foundrycompareprime =  DataPool(
           series=
            [{'options': {

            'source': FoundrycomparePrime},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrycompareprime,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Prime Aluminum Purchase amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrycompareprime,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Prime Aluminum Purchase amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def foundrycompareLog(request):
    foundrycomparelog =  DataPool(
           series=
            [{'options': {

            'source': FoundrycompareLog},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = foundrycomparelog,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Logs and Billets Purchase amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = foundrycomparelog,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Logs and Billets Purchase amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiononeItem(request):
    extrusiononeitem =  DataPool(
           series=
            [{'options': {
            'source': ExtrusiononeItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiononeitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiononeitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiontwoItem(request):
    extrusiontwoitem =  DataPool(
           series=
            [{'options': {
            'source': ExtrusiontwoItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiontwoitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiontwoitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusionthreeItem(request):
    extrusionthreeitem =  DataPool(
           series=
            [{'options': {
            'source': ExtrusionthreeItem.objects.all()},
                'terms': [{'item': 'item',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusionthreeitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'item': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount each item in USD'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusionthreeitem,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'item': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount each item in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'item'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiononetopItem(request):
    extrusiononetopitem =  DataPool(
           series=
            [{'options': {

            'source': ExtrusiononetopItem},

                'terms': [{'month': 'month',
                'Maintenance and Repairs': 'maintenance',
                'Oil and Hydraulics': 'oil',
                'Saw Blades': 'saw',
                'Shop Supplies':'shop',
                'Lubricants':'lubricant',
                'Lift Truck Expense':'lift',
                'Outside Mechanical':'outside'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiononetopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount for top7 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiononetopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount for top7 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiontwotopItem(request):
    extrusiontwotopitem =  DataPool(
           series=
            [{'options': {

            'source': ExtrusiontwotopItem},

                'terms': [{'month': 'month',
                'Maintenance and Repairs': 'maintenance',
                'Oil and Hydraulics': 'oil',
                'Saw Blades': 'saw',
                'Shop Supplies':'shop',
                'Lubricants':'lubricant',
                'Lift Truck Expense':'lift',
                'Outside Mechanical':'outside'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiontwotopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount for top7 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiontwotopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount for top7 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusionthreetopItem(request):
    extrusionthreetopitem =  DataPool(
           series=
            [{'options': {

            'source': ExtrusionthreetopItem},

                'terms': [{'month': 'month',
                'Maintenance and Repairs': 'maintenance',
                'Oil and Hydraulics': 'oil',
                'Saw Blades': 'saw',
                'Shop Supplies':'shop',
                'Lubricants':'lubricant',
                'Lift Truck Expense':'lift',
                'Outside Mechanical':'outside'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusionthreetopitem,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount for top7 items each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusionthreetopitem,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'Maintenance and Repairs','Oil and Hydraulics','Saw Blades','Shop Supplies','Lubricants','Lift Truck Expense','Outside Mechanical']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount for top7 items each month in USD - bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiononeMonth(request):
    extrusiononemonth =  DataPool(
           series=
            [{'options': {

            'source': ExtrusiononeMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiononemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiononemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Extrusion Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusiontwoMonth(request):
    extrusiontwomonth =  DataPool(
           series=
            [{'options': {

            'source': ExtrusiontwoMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusiontwomonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusiontwomonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Extrusion Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusionthreeMonth(request):
    extrusionthreemonth =  DataPool(
           series=
            [{'options': {

            'source': ExtrusionthreeMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusionthreemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusionthreemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Extrusion Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusionallMonth(request):
    extrusionallmonth =  DataPool(
           series=
            [{'options': {

            'source': ExtrusionallMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusionallmonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Extrusion Purchase amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusionallmonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Extrusion Purchase amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusioncompareMonth(request):
    extrusioncomparemonth =  DataPool(
           series=
            [{'options': {

            'source': ExtrusioncompareMonth},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusioncomparemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Extrusion purchase amount compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusioncomparemonth,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Extrusion purchase amount compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def extrusioncompareMain(request):
    extrusioncomparemain =  DataPool(
           series=
            [{'options': {

            'source': ExtrusioncompareMain},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = extrusioncomparemain,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Maintanence Cost amount in Extrusion Compare each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = extrusioncomparemain,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Maintanence Cost amount in Extrusion Compare each month in USD - Bar Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneRep(request):
    salesonerep =  DataPool(
           series=
            [{'options': {
            'source': SalesoneRep.objects.all()},
                'terms': [{'rep': 'rep',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonerep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'rep': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Sales Amount each Regional Sales Representative in USD'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonerep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'rep': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Sales Amount each Regional Sales Representative in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})



def salestwoRep(request):
    salestworep =  DataPool(
           series=
            [{'options': {
            'source': SalestwoRep.objects.all()},
                'terms': [{'rep': 'rep',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestworep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'rep': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Sales Amount each Regional Sales Representative in USD'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestworep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'rep': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Sales Amount each Regional Sales Representative in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeRep(request):
    salesthreerep =  DataPool(
           series=
            [{'options': {
            'source': SalesthreeRep.objects.all()},
                'terms': [{'rep': 'rep',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreerep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'rep': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Sales Amount each Regional Sales Representative in USD'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreerep,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'rep': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Sales Amount each Regional Sales Representative in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'rep'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneCustomer(request):
    salesonecustomer =  DataPool(
           series=
            [{'options': {
            'source': SalesoneCustomer.objects.all()},
                'terms': [{'customer': 'customer',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonecustomer,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'customer': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 Sales Amount each Company in USD'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonecustomer,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'customer': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 Sales Amount each Company in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoCustomer(request):
    salestwocustomer =  DataPool(
           series=
            [{'options': {
            'source': SalestwoCustomer.objects.all()},
                'terms': [{'customer': 'customer',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwocustomer,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'customer': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 Sales Amount each Company in USD'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwocustomer,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'customer': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 Sales Amount each Company in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeCustomer(request):
    salesthreecustomer =  DataPool(
           series=
            [{'options': {
            'source': SalesthreeCustomer.objects.all()},
                'terms': [{'customer': 'customer',
                'amount': 'amount'}]
                }       
             ]) 
      
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreecustomer,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'customer': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 Sales Amount each Company in USD'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   

            )  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreecustomer,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'customer': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 Sales Amount each Company in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'customer'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
            )                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneMonth(request):
    salesonemonth =  DataPool(
           series=
            [{'options': {

            'source': SalesoneMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoMonth(request):
    salestwomonth =  DataPool(
           series=
            [{'options': {

            'source': SalestwoMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwomonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwomonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeMonth(request):
    salesthreemonth =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreemonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreemonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallMonth(request):
    salesallmonth =  DataPool(
           series=
            [{'options': {

            'source': SalesallMonth},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesallmonth,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesallmonth,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def salesoneBl(request):
    salesonebl =  DataPool(
           series=
            [{'options': {

            'source': SalesoneBl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonebl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for BL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonebl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for BL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoBl(request):
    salestwobl =  DataPool(
           series=
            [{'options': {

            'source': SalestwoBl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwobl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for BL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwobl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for BL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeBl(request):
    salesthreebl =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeBl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreebl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for BL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreebl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for BL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallBl(request):
    salesallbl =  DataPool(
           series=
            [{'options': {

            'source': SalesallBl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesallbl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for BL Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesallbl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for BL Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareBl(request):
    salescomparebl =  DataPool(
           series=
            [{'options': {

            'source': SalescompareBl},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescomparebl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for BL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescomparebl,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for BL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})


def salesoneCl(request):
    salesonecl =  DataPool(
           series=
            [{'options': {

            'source': SalesoneCl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonecl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for CL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonecl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for CL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoCl(request):
    salestwocl =  DataPool(
           series=
            [{'options': {

            'source': SalestwoCl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwocl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for CL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwocl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for CL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeCl(request):
    salesthreecl =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeCl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreecl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for CL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreecl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for CL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallCl(request):
    salesallcl =  DataPool(
           series=
            [{'options': {

            'source': SalesallCl},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesallcl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for CL Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesallcl,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for CL Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareCl(request):
    salescomparecl =  DataPool(
           series=
            [{'options': {

            'source': SalescompareCl},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescomparecl,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for CL each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescomparecl,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for CL each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneDa(request):
    salesoneda =  DataPool(
           series=
            [{'options': {

            'source': SalesoneDa},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesoneda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for DA each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesoneda,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for DA each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoDa(request):
    salestwoda =  DataPool(
           series=
            [{'options': {

            'source': SalestwoDa},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwoda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for DA each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwoda,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for DA each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeDa(request):
    salesthreeda =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeDa},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreeda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for DA each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreeda,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for DA each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallDa(request):
    salesallda =  DataPool(
           series=
            [{'options': {

            'source': SalesallDa},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesallda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for DA Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesallda,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for DA Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareDa(request):
    salescompareda =  DataPool(
           series=
            [{'options': {

            'source': SalescompareDa},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescompareda,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for DA each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescompareda,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for DA each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneS1(request):
    salesones1 =  DataPool(
           series=
            [{'options': {

            'source': SalesoneS1},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesones1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S1 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesones1,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S1 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoS1(request):
    salestwos1 =  DataPool(
           series=
            [{'options': {

            'source': SalestwoS1},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwos1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S1 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwos1,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S1 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeS1(request):
    salesthrees1 =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeS1},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthrees1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S1 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthrees1,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S1 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallS1(request):
    salesalls1 =  DataPool(
           series=
            [{'options': {

            'source': SalesallS1},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesalls1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S1 Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesalls1,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S1 Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareS1(request):
    salescompares1 =  DataPool(
           series=
            [{'options': {

            'source': SalescompareS1},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescompares1,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S1 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescompares1,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S1 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneS2(request):
    salesones2 =  DataPool(
           series=
            [{'options': {

            'source': SalesoneS2},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesones2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S2 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesones2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S2 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoS2(request):
    salestwos2 =  DataPool(
           series=
            [{'options': {

            'source': SalestwoS2},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwos2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S2 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwos2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S2 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeS2(request):
    salesthrees2 =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeS2},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthrees2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S2 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthrees2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S2 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallS2(request):
    salesalls2 =  DataPool(
           series=
            [{'options': {

            'source': SalesallS2},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesalls2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S2 Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesalls2,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S2 Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareS2(request):
    salescompares2 =  DataPool(
           series=
            [{'options': {

            'source': SalescompareS2},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescompares2,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S2 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescompares2,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S2 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneS3(request):
    salesones3 =  DataPool(
           series=
            [{'options': {

            'source': SalesoneS3},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesones3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S3 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesones3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S3 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoS3(request):
    salestwos3 =  DataPool(
           series=
            [{'options': {

            'source': SalestwoS3},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwos3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S3 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwos3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S3 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeS3(request):
    salesthrees3 =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeS3},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthrees3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S3 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthrees3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S3 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallS3(request):
    salesalls3 =  DataPool(
           series=
            [{'options': {

            'source': SalesallS3},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesalls3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S3 Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesalls3,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S3 Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareS3(request):
    salescompares3 =  DataPool(
           series=
            [{'options': {

            'source': SalescompareS3},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescompares3,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S3 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescompares3,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S3 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneS4(request):
    salesones4 =  DataPool(
           series=
            [{'options': {

            'source': SalesoneS4},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesones4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S4 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesones4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount for S4 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoS4(request):
    salestwos4 =  DataPool(
           series=
            [{'options': {

            'source': SalestwoS4},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwos4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S4 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwos4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount for S4 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeS4(request):
    salesthrees4 =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeS4},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthrees4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount for S4 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthrees4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount each month for S4 in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallS4(request):
    salesalls4 =  DataPool(
           series=
            [{'options': {

            'source': SalesallS4},

                'terms': [{'month': 'month',
                'amount': 'amount'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesalls4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S4 Each Month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount Total'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesalls4,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'amount']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 Sales amount for S4 Each Month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount total'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salescompareS4(request):
    salescompares4 =  DataPool(
           series=
            [{'options': {

            'source': SalescompareS4},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salescompares4,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S4 each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salescompares4,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare for S4 each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesoneDep(request):
    salesonedep =  DataPool(
           series=
            [{'options': {

            'source': SalesoneDep},

                'terms': [{'month': 'month',
                'extrusion': 'extrusion',
                'fabrication': 'fabrication',
                'anodizing': 'anodizing'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesonedep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
            chart_options =
              {'title': {
                   'text': '2019 sales amount three departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesonedep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2019 sales amount three departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salestwoDep(request):
    salestwodep =  DataPool(
           series=
            [{'options': {

            'source': SalestwoDep},

                'terms': [{'month': 'month',
                'extrusion': 'extrusion',
                'fabrication': 'fabrication',
                'anodizing': 'anodizing'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salestwodep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
            chart_options =
              {'title': {
                   'text': '2018 sales amount three departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salestwodep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2018 sales amount three departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesthreeDep(request):
    salesthreedep =  DataPool(
           series=
            [{'options': {

            'source': SalesthreeDep},

                'terms': [{'month': 'month',
                'extrusion': 'extrusion',
                'fabrication': 'fabrication',
                'anodizing': 'anodizing'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesthreedep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017 sales amount three departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesthreedep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017 sales amount three departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesallDep(request):
    salesalldep =  DataPool(
           series=
            [{'options': {

            'source': SalesallDep},

                'terms': [{'month': 'month',
                'extrusion': 'extrusion',
                'fabrication': 'fabrication',
                'anodizing': 'anodizing'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1701: 'Jan 2017', 1702: 'Feb 2017', 1703: 'Mar 2017', 1704: 'Apr 2017', 1705: 'May 2017', 1706: 'Jun 2017',
                1707: 'Jul 2017', 1708: 'Aug 2017', 1709: 'Sep 2017', 1710: 'Oct 2017', 1711: 'Nov 2017', 1712: 'Dec 2017',
                1801: 'Jan 2018', 1802: 'Feb 2018', 1803: 'Mar 2018', 1804: 'Apr 2018', 1805: 'May 2018', 1806: 'Jun 2018',
                1807: 'Jul 2018', 1808: 'Aug 2018', 1809: 'Sep 2018', 1810: 'Oct 2018', 1811: 'Nov 2018', 1812: 'Dec 2018',
                1901: 'Jan 2019', 1902: 'Feb 2019', 1903: 'Mar 2019', 1904: 'Apr 2019', 1905: 'May 2019', 1906: 'Jun 2019',
                1907: 'Jul 2019', 1908: 'Aug 2019', 1909: 'Sep 2019', 1910: 'Oct 2019', 1911: 'Nov 2019', 1912: 'Dec 2019',
            #2001: 'Jan 2020', 2002: 'Feb 2020', 2003: 'Mar 2020', 2004: 'Apr 2020',
            #2005: 'May 2020', 2006: 'Jun 2020',2007: 'Jul 2020', 2008: 'Aug 2020',
            #2009: 'Sep 2020', 2010: 'Oct 2020', 2011: 'Nov 2020', 2012: 'Dec 2020'
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesalldep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount three departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesalldep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'extrusion','fabrication','anodizing']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount three departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesextrusionDep(request):
    salesextrusiondep =  DataPool(
           series=
            [{'options': {

            'source': SalesextrusionDep},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesextrusiondep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare extrusion departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesextrusiondep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare extrusion departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesfabricationDep(request):
    salesfabricationdep =  DataPool(
           series=
            [{'options': {

            'source': SalesfabricationDep},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesfabricationdep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare fabrication departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesfabricationdep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare fabrication departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})

def salesanodizingDep(request):
    salesanodizingdep =  DataPool(
           series=
            [{'options': {

            'source': SalesanodizingDep},

                'terms': [{'month': 'month',
                '2017': 'three',
                '2018': 'two',
                '2019': 'one'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {
                1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec',
                 }
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = salesanodizingdep,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare anodizing departments each month in USD'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = salesanodizingdep,
            series_options =
              [{'options':{
                  'type': 'column',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    '2017','2018','2019']
                  }}],
    
            chart_options =
              {'title': {
                   'text': '2017-2019 sales amount compare anodizing departments each month in USD - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'month'}},
               'yAxis': {
                   'title': {'text': 'amount'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})
