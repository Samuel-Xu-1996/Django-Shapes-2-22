from django.db import models

class Sales(models.Model):
    Customerno = models.CharField('Customerno', max_length=30)
    CompanyName = models.CharField('Companyname', max_length=50)
    DieNumber = models.CharField('DieNumber', max_length=30)
    Invoiceno = models.CharField('Invoiceno', max_length=30)
    Salesorderno = models.CharField('Salesorderno', max_length=30)
    LinenoAlt = models.CharField('LinenoAlt', max_length=30)
    Partno = models.CharField('Partno', max_length=30)
    Partdescr = models.CharField('Partdescr', max_length=50)
    Dateshipped = models.DateField('Dateshipped')
    Invoicedate = models.DateField('Invoicedate')
    QtyShipped = models.IntegerField('QtyShipped')
    CalcActualWgt = models.FloatField('CalcActualWgt')
    CalcTheorWgt = models.FloatField('CalcTheorWgt')
    CalcPrice = models.FloatField('CalcPrice')
    ExtrusionRevenue = models.FloatField('ExtrusionRevenue')
    PriceperLb = models.FloatField('PriceperLb')
    FabricationLbs = models.FloatField('FabricationLbs')
    FabricationRevenue = models.FloatField('FabricationRevenue')
    PaintLbs = models.FloatField('PaintLbs')
    PaintRevenue = models.FloatField('PaintRevenue')
    AnodizingSqFt = models.FloatField('AnodizingSqFt')
    AnodizingRevenue = models.FloatField('AnodizingRevenue')
    IngotPrice = models.FloatField('IngotPrice ')
    Press = models.CharField('Press', max_length=30)
    Ordertype = models.CharField('Ordertype', max_length=30)
    Unitofmeas = models.CharField('Unitofmeas', max_length=30)
    Productline = models.CharField('Productline', max_length=30)
    Shiptono = models.CharField('Shiptono', max_length=30)
    ShiptoState = models.CharField('ShipToState', max_length=30)
    RSM = models.CharField('RSM', max_length=30)
    RSMName = models.CharField('RSMName', max_length=30)


    class Meta:
        verbose_name = 'sales report'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Customerno
