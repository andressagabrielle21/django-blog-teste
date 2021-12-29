from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    # class indica que estamos criando um objeto
    # Post é o nome do modelo. POde ser nome diferente, sempre iniciando com letra maiúscula 
    # (models.Model) significa que Post é um modelo Django, ou seja, será guardado no BD
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #O método chamado Publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title