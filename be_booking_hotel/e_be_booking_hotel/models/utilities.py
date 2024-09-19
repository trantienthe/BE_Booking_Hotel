from django.db import models

class Utilities(models.Model):
    utilities_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
