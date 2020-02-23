from django.db import models

class Purchase(models.Model):
    PO = models.CharField('PO', max_length=30)
    VendorNo = models.CharField('VendorNo', max_length=30)
    VendorName = models.CharField('VendorName', max_length=50)
    Line = models.CharField('Line', max_length=50)
    Partno = models.CharField('Partno', max_length=50)
    Partdescr = models.CharField('Partdescr', max_length=50)
    GLAccountno = models.CharField('GLAccountno', max_length=50)
    Datepromised = models.DateField('Datepromised')
    Qtyonorder = models.IntegerField('Qtyonorder')
    Price = models.FloatField('Price')
    LineAmount = models.IntegerField('LineAmount')
    Requestedby = models.CharField('Requestedby', max_length=100)
    Buyer = models.CharField('Buyer', max_length=100)
    Status = models.CharField('Status', max_length=30)
    Projectno = models.CharField('Projectno', max_length=100)
    ProjectDesc = models.CharField('ProjectDesc', max_length=200)

    class Meta:
        verbose_name = 'purchase report'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Vendor_No
