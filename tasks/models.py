from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  @property
  def description_decrypted(self):
    f = Fernet(settings.ECRYPTED_KEY)
    description_decrypted = f.decrypt(self.description.encode('utf-8'))
    description_decoded = description_decrypted.decode('utf-8')
    return description_decoded

  def __str__(self):
    return self.title + ' - ' + self.user.username
