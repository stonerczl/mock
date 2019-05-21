from django.db import models

# Create your models here.
class Mocktest(models.Model):
    url = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    server = models.CharField(max_length=10,default='')
    request_body = models.CharField(max_length=500)
    response_body = models.CharField(max_length=500)
    time_delay = models.FloatField()
    add_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=100,default='')