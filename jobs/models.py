from django.db import models

class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    applied_date = models.DateField(auto_now_add=True)
    status_choices = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interview'),
        ('OFFER', 'Offer'),
        ('REJECTED', 'Rejected'),
    ]
    status=models.CharField(max_length=20,choices=status_choices,default='APPLIED')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"
