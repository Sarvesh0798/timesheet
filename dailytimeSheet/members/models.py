from django.db import models

class Members(models.Model):
  dte=models.CharField(max_length=9)
  name=models.CharField(max_length=30)
  ve = models.CharField(max_length=5)
  vo = models.CharField(max_length=5)
  oe = models.CharField(max_length=5)
  oo = models.CharField(max_length=5)
  vt = models.CharField(max_length=5)
  ot = models.CharField(max_length=5)
  tt = models.CharField(max_length=5)
