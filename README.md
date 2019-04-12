# mongoengine_get_or_create
mongoengine `get_or_create` filter query

MongoEngine does not has get_or_create filter query like django model query. 

Follow steps to make it work in mongoengine:

Add `custome_filters.py` into your project and import `GetOrCreateQuerySet` into models file

Then add `GetOrCreateQuerySet` into `meta`

Now You can use `get_or_create` filter query into mongoengine

See the example file code in `models.py`
