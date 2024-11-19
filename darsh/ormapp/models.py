from django.db import models
from django.contrib import admin
class bankloan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=30)
    loan_amt = models.IntegerField()
    cust_name = models.CharField(max_length=30)
    cust_acno = models.IntegerField()
class bankloanAdmin(admin.ModelAdmin):
    list_display = ('loan_id','loan_type','loan_amt','cust_name','cust_acno')