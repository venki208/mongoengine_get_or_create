from mongoengine import *

from .custome_filters import GetOrCreateQuerySet


class Demo(Document):
    first_name = StringField()
    last_name = StringField()
    email = EmailField()

    meta = {
        'queryset_class': GetOrCreateQuerySet
    }

    def __str__(self):
        return self.email



Query:

obj, is_created = Demo.objects.get_or_create(email = 'xyz@gmail.com')

obj --> contains table object
is_created --> contains status of object (i.e; if it creates returns `True` else `False`)
