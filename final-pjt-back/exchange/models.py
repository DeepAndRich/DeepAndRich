from django.db import models

class ExchangeRateInfo(models.Model):
  cur_unit = models.TextField(unique=True)
  cur_nm = models.TextField()
  deal_bas_r = models.TextField()