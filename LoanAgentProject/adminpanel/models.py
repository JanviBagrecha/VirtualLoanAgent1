from django.db import models

# Create your models here.
class Loanagent(models.Model):
    name = models.CharField(max_length=100) 
    interest_pl = models.CharField(max_length=100)
    interest_bl = models.CharField(max_length=100)
    interest_hl = models.CharField(max_length=100)
    interest_el = models.CharField(max_length=100)
    interest_vl = models.CharField(max_length=100)
    principal_pl = models.CharField(max_length=100)
    principal_bl = models.CharField(max_length=100)
    principal_hl = models.CharField(max_length=100)
    principal_el = models.CharField(max_length=100)
    principal_vl = models.CharField(max_length=100)
    time_pl = models.CharField(max_length=100)
    time_bl = models.CharField(max_length=100)
    time_hl = models.CharField(max_length=100)
    time_el = models.CharField(max_length=100)
    time_vl = models.CharField(max_length=100)

    class Meta:
        db_table="bankdetails"