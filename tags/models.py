from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=50)


class TaggedItem(models.Model):
    # What tag applied to what object:
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type of the object (product, blog, video):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    content_object = GenericForeignKey()
    
