from django.contrib import admin
from .models import SalesReport, MonthlyWeatherByCity,SalesCompany, PurchaseCode, PurchaseReport, InventoryReport, MonthlyRevenue,\
     OrderRep, OrderCustomer, OrderDate, OrderBl, OrderCl, OrderDa, OrderS1, OrderS2, OrderS3, OrderS4, PivotBudget,\
     OveralloneDep, OveralltwoDep, OverallthreeDep,\
     FoundryoneMonth, FoundrytwoMonth, FoundrythreeMonth, FoundryallMonth, FoundrycompareMonth,\
     FoundryoneVendor, FoundrytwoVendor, FoundrythreeVendor, FoundryallVendor,\
     FoundryoneItem, FoundrytwoItem, FoundrythreeItem, FoundryallItem,\
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

admin.site.register(SalesReport)
admin.site.register(MonthlyWeatherByCity)
admin.site.register(PurchaseCode)
admin.site.register(SalesCompany)
admin.site.register(PurchaseReport)
admin.site.register(InventoryReport)
admin.site.register(MonthlyRevenue)

admin.site.register(OrderRep)
admin.site.register(OrderCustomer)
admin.site.register(OrderDate)
admin.site.register(OrderBl)
admin.site.register(OrderCl)
admin.site.register(OrderDa)
admin.site.register(OrderS1)
admin.site.register(OrderS2)
admin.site.register(OrderS3)
admin.site.register(OrderS4)

admin.site.register(PivotBudget)

admin.site.register(OveralloneDep)
admin.site.register(OveralltwoDep)
admin.site.register(OverallthreeDep)

admin.site.register(FoundryoneMonth)
admin.site.register(FoundrytwoMonth)
admin.site.register(FoundrythreeMonth)
admin.site.register(FoundryallMonth)
admin.site.register(FoundrycompareMonth)

admin.site.register(FoundryoneVendor)
admin.site.register(FoundrytwoVendor)
admin.site.register(FoundrythreeVendor)
admin.site.register(FoundryallVendor)

admin.site.register(FoundryoneItem)
admin.site.register(FoundrytwoItem)
admin.site.register(FoundrythreeItem)
admin.site.register(FoundryallItem)

admin.site.register(FoundryonetopItem)
admin.site.register(FoundrytwotopItem)
admin.site.register(FoundrythreetopItem)

admin.site.register(FoundryoneExpense)
admin.site.register(FoundrytwoExpense)
admin.site.register(FoundrythreeExpense)

admin.site.register(FoundrycompareScrap)
admin.site.register(FoundrycomparePrime)
admin.site.register(FoundrycompareLog)

admin.site.register(FoundrymainCompare)
admin.site.register(FoundrymainAll)
admin.site.register(FoundrymainMini)

admin.site.register(ExtrusiononeItem)
admin.site.register(ExtrusiontwoItem)
admin.site.register(ExtrusionthreeItem)

admin.site.register(ExtrusiononetopItem)
admin.site.register(ExtrusiontwotopItem)
admin.site.register(ExtrusionthreetopItem)

admin.site.register(ExtrusiononeMonth)
admin.site.register(ExtrusiontwoMonth)
admin.site.register(ExtrusionthreeMonth)
admin.site.register(ExtrusioncompareMonth)
admin.site.register(ExtrusionallMonth)

admin.site.register(ExtrusioncompareMain)

admin.site.register(SalesoneRep)
admin.site.register(SalestwoRep)
admin.site.register(SalesthreeRep)
admin.site.register(SalesoneCustomer)
admin.site.register(SalestwoCustomer)
admin.site.register(SalesthreeCustomer)
admin.site.register(SalesoneMonth)
admin.site.register(SalestwoMonth)
admin.site.register(SalesthreeMonth)
admin.site.register(SalesallMonth)

admin.site.register(SalesoneBl)
admin.site.register(SalestwoBl)
admin.site.register(SalesthreeBl)
admin.site.register(SalesallBl)
admin.site.register(SalescompareBl)
admin.site.register(SalesoneCl)
admin.site.register(SalestwoCl)
admin.site.register(SalesthreeCl)
admin.site.register(SalesallCl)
admin.site.register(SalescompareCl)
admin.site.register(SalesoneDa)
admin.site.register(SalestwoDa)
admin.site.register(SalesthreeDa)
admin.site.register(SalesallDa)
admin.site.register(SalescompareDa)
admin.site.register(SalesoneS1)
admin.site.register(SalestwoS1)
admin.site.register(SalesthreeS1)
admin.site.register(SalesallS1)
admin.site.register(SalescompareS1)
admin.site.register(SalesoneS2)
admin.site.register(SalestwoS2)
admin.site.register(SalesthreeS2)
admin.site.register(SalesallS2)
admin.site.register(SalescompareS2)
admin.site.register(SalesoneS3)
admin.site.register(SalestwoS3)
admin.site.register(SalesthreeS3)
admin.site.register(SalesallS3)
admin.site.register(SalescompareS3)
admin.site.register(SalesoneS4)
admin.site.register(SalestwoS4)
admin.site.register(SalesthreeS4)
admin.site.register(SalesallS4)
admin.site.register(SalescompareS4)

admin.site.register(SalesoneDep)
admin.site.register(SalestwoDep)
admin.site.register(SalesthreeDep)
admin.site.register(SalesallDep)

admin.site.register(SalesextrusionDep)
admin.site.register(SalesfabricationDep)
admin.site.register(SalesanodizingDep)
