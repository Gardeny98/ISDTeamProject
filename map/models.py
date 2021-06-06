from django.contrib.gis.db import models

# Create your models here.
class MapCity(models.Model):
    id = models.BigAutoField(primary_key=True)
    sigungu_en = models.CharField(db_column='sigungu_EN', max_length=200)  # Field name made lowercase.
    sigungu_kr = models.DateTimeField(db_column='sigungu_KR')  # Field name made lowercase.
    geometry = models.GeometryField()
