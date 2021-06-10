from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from dashboards.models import *

trainer, created = Group.objects.get_or_create(name='trainer')
economist, created = Group.objects.get_or_create(name='economist')
manager, created = Group.objects.get_or_create(name='manager')
