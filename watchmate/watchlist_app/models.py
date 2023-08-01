from django.db import models

# Create your models here.


class Movie(models.Model):
    """Defines movie table"""
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return "<'%s' ('%s', '%s', '%s')>" % (
            self.__class__.__name__, self.name, self.active, self.pk
        )
