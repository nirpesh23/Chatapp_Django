from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='CustomerProfilePic/',blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)

    # def full_name(self):
    #     return self.user.get_full_name()

    # def __str__(self):
    #     return self.user.full_name



    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name