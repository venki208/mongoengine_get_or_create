from mongoengine.queryset import QuerySet


class GetOrCreateQuerySet(QuerySet):
    '''
    Custome Query for getting or creating the object
    '''

    def get_or_create(self, *args, **kwargs):
        obj = self.filter(*args, **kwargs).first()
        if obj:
            return obj, False
        else:
            obj = self.create(*args, **kwargs)
            return obj, True
