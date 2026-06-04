from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#dob validator function
def validate_dob(value):
    current_date = timezone.localdate()
    if value >= current_date:
        raise ValidationError("Date of birth cannot be in future")
    
class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(verbose_name="Full Name" , max_length=200)
    email_add = models.EmailField(verbose_name="Email",max_length=100,)
    dob = models.DateField(verbose_name="Date of Birth", validators=[validate_dob])
    record_date = models.DateTimeField(auto_now_add=True, null=True)
    glucose = models.DecimalField(max_digits=8, decimal_places=2)
    haemoglobin = models.DecimalField(max_digits=8, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=8, decimal_places=2)
    remarks = models.CharField(null=True)