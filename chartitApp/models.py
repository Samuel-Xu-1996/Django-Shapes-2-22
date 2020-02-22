from django.db import models

class SalesReport(models.Model):
    month = models.IntegerField()
    sales = models.FloatField()
    customer = models.CharField(max_length= 25)


class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    WABASH_sales = models.DecimalField(max_digits=10, decimal_places=1)
    UHAUL_sales = models.DecimalField(max_digits=10, decimal_places=1)
    WABASH = models.DecimalField(max_digits=10, decimal_places=1)

class SalesCompany(models.Model):
    sales = models.FloatField()
    customer = models.CharField(max_length= 25)

class PurchaseCode(models.Model):
    purchase = models.FloatField()
    department = models.CharField(max_length= 25)

class PurchaseReport(models.Model):
    purchase = models.FloatField()
    month = models.IntegerField()
    customer = models.CharField(max_length= 25)

class InventoryReport(models.Model):
    inventory = models.FloatField()
    month = models.IntegerField()

class MonthlyRevenue(models.Model):
    revenue = models.FloatField()
    month = models.IntegerField()

class OrderRep(models.Model):
    rep = models.CharField(max_length = 25)
    weight = models.FloatField()

class OrderCustomer(models.Model):
    customer = models.CharField(max_length = 50)
    weight = models.FloatField()
    
class OrderDate(models.Model):
    date = models.IntegerField()
    weight = models.FloatField()

class OrderBl(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderCl(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderDa(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderS1(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderS2(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderS3(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class OrderS4(models.Model):
    month = models.IntegerField()
    weight = models.FloatField()

class PivotBudget(models.Model):
    month = models.IntegerField()
    Companyname = models.CharField(max_length=255)
    Datepromised = models.DateField()
    OrderLbs = models.FloatField()
    Press = models.CharField(max_length=255)

class OveralloneDep(models.Model):
    department = models.CharField(max_length=255)
    amount = models.FloatField()

class OveralltwoDep(models.Model):
    department = models.CharField(max_length=255)
    amount = models.FloatField()

class OverallthreeDep(models.Model):
    department = models.CharField(max_length=255)
    amount = models.FloatField()

class FoundrymainCompare(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()
    zero = models.FloatField()

class FoundrymainMini(models.Model):
    year = models.IntegerField()
    cost = models.FloatField()

class FoundrymainAll(models.Model):
    month = models.IntegerField()
    cost = models.FloatField()

class FoundryoneMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class FoundrytwoMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class FoundrythreeMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class FoundryallMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class FoundrycompareMonth(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class FoundryoneVendor(models.Model):
    vendor = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrytwoVendor(models.Model):
    vendor = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrythreeVendor(models.Model):
    vendor = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundryallVendor(models.Model):
    vendor = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundryoneItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrytwoItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrythreeItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundryoneExpense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrytwoExpense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrythreeExpense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundryonetopItem(models.Model):
    month = models.IntegerField()
    prime = models.FloatField()
    scrap = models.FloatField()
    log = models.FloatField()

class FoundrytwotopItem(models.Model):
    month = models.IntegerField()
    prime = models.FloatField()
    scrap = models.FloatField()
    log = models.FloatField()

class FoundrythreetopItem(models.Model):
    month = models.IntegerField()
    prime = models.FloatField()
    scrap = models.FloatField()
    log = models.FloatField()

class FoundryallItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class FoundrycompareScrap(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class FoundrycomparePrime(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class FoundrycompareLog(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class ExtrusiononeItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class ExtrusiontwoItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class ExtrusionthreeItem(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.FloatField()

class ExtrusiononetopItem(models.Model):
    month = models.IntegerField()
    maintenance = models.FloatField()
    oil = models.FloatField()
    saw = models.FloatField()
    shop = models.FloatField()
    lubricant = models.FloatField()
    lift = models.FloatField()
    outside = models.FloatField()

class ExtrusiontwotopItem(models.Model):
    month = models.IntegerField()
    maintenance = models.FloatField()
    oil = models.FloatField()
    saw = models.FloatField()
    shop = models.FloatField()
    lubricant = models.FloatField()
    lift = models.FloatField()
    outside = models.FloatField()

class ExtrusionthreetopItem(models.Model):
    month = models.IntegerField()
    maintenance = models.FloatField()
    oil = models.FloatField()
    saw = models.FloatField()
    shop = models.FloatField()
    lubricant = models.FloatField()
    lift = models.FloatField()
    outside = models.FloatField()

class ExtrusiononeMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class ExtrusiontwoMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class ExtrusionthreeMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class ExtrusionallMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class ExtrusioncompareMonth(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class ExtrusioncompareMain(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneRep(models.Model):
    rep = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalestwoRep(models.Model):
    rep = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalesthreeRep(models.Model):
    rep = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalesoneCustomer(models.Model):
    customer = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalestwoCustomer(models.Model):
    customer = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalesthreeCustomer(models.Model):
    customer = models.CharField(max_length = 50)
    amount = models.FloatField()

class SalesoneMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallMonth(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesoneBl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoBl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeBl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallBl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareBl(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneCl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoCl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeCl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallCl(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareCl(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneDa(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoDa(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeDa(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallDa(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareDa(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneS1(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoS1(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeS1(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallS1(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareS1(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneS2(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoS2(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeS2(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallS2(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareS2(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneS3(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoS3(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeS3(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallS3(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareS3(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneS4(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalestwoS4(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesthreeS4(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalesallS4(models.Model):
    month = models.IntegerField()
    amount = models.FloatField()

class SalescompareS4(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesoneDep(models.Model):
    month = models.IntegerField()
    extrusion = models.FloatField()
    fabrication = models.FloatField()
    anodizing = models.FloatField()

class SalestwoDep(models.Model):
    month = models.IntegerField()
    extrusion = models.FloatField()
    fabrication = models.FloatField()
    anodizing = models.FloatField()

class SalesthreeDep(models.Model):
    month = models.IntegerField()
    extrusion = models.FloatField()
    fabrication = models.FloatField()
    anodizing = models.FloatField()

class SalesallDep(models.Model):
    month = models.IntegerField()
    extrusion = models.FloatField()
    fabrication = models.FloatField()
    anodizing = models.FloatField()

class SalesextrusionDep(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesfabricationDep(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()

class SalesanodizingDep(models.Model):
    month = models.IntegerField()
    one = models.FloatField()
    two = models.FloatField()
    three = models.FloatField()    
