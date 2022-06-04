from datetime import date
from django.db import models
from django.utils.text import slugify


class Activity(models.Model):
    org_name                = models.ManyToManyField('Organization')
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

    @property
    def Is_Past(self):
        today = date.today()
        if self.starttime.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing

    class Meta:
        ordering = ["-starttime"]



class Organization(models.Model):
    org_name = models.CharField(max_length=64, null=False, blank=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    authorized = models.CharField(max_length=64, null=False, blank=False)
    org_image = models.ImageField(upload_to='organization', blank=True, null=True)
    address = models.TextField()
    org_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.org_name) + " ( " + str(self.authorized) + " )"