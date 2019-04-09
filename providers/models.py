from django.db import models

# Create your models here.
# class PrescriberInfo(models.Model):
#     f_name = models.TextField()
#     l_name = models.TextField()
#     gender = models.TextField(max_length=1)
#     state = models.TextField(max_length=2)
#     credentials = models.TextField()
#     opioid_prescriber = models.IntegerField()
#     total_prescriptions = models.IntegerField()

#     # Returns the full name of the provider
#     def get_full_name(self):
#         full_name = self.f_name + ' ' + self.l_name
#         return full_name