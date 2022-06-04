from datetime import date
from django.db import models
from django.utils.text import slugify


class Activity(models.Model):
    activity_name           = models.CharField(max_length=64, null=False, blank=False)
    activity_image          = models.ImageField(upload_to='activity', blank=True, null=True)
    active                  = models.BooleanField()
    address                 = models.TextField()
    description             = models.TextField()
    starttime               = models.DateTimeField(auto_now_add=False)
    endtime                 = models.DateTimeField(auto_now_add=False)
    slug                    = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.activity_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.activity_name)
        super().save(*args, **kwargs)



