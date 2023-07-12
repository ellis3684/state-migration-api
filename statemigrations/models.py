from django.db import models


class StateMigration(models.Model):
    year = models.IntegerField()
    previous_state = models.CharField(max_length=50)
    previous_division = models.CharField(max_length=2)
    estimate = models.IntegerField()
    margin_of_error = models.FloatField()
