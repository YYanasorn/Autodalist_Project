from django.db import models
from django.utils import timezone

class Parameter(models.Model):
    time = models.DateTimeField(default=timezone.now)
    comp_number = models.CharField(max_length=255)
    hour_meter = models.FloatField(default=0.0)
    inlet_pressure = models.FloatField(default=0.0)
    stage_1_pressure = models.FloatField(default=0.0)
    discharge_pressure = models.FloatField(default=0.0)
    compressor_oil_presure = models.FloatField(default=0.0)
    st_1_1_temp = models.FloatField(default=0.0)
    st_1_2_temp = models.FloatField(default=0.0)
    st_2_1_temp = models.FloatField(default=0.0)
    st_2_2_temp = models.FloatField(default=0.0)
    gas_detector = models.FloatField(default=0.0)
    comp_oil_temp = models.FloatField(default=0.0)
    motor_current = models.FloatField(default=0.0)


    def __str__(self):
        return self.comp_number + '' + str(self.hour_meter)