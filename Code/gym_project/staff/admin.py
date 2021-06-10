from staff.models import InventoryItem
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from dashboards.models import *
from django.contrib.auth.models import User

trainer, tcreated = Group.objects.get_or_create(name='trainer')
economist, ecreated = Group.objects.get_or_create(name='economist')
manager, mcreated = Group.objects.get_or_create(name='manager')

exercise_type = ContentType.objects.get_for_model(Exercise)
routine_type = ContentType.objects.get_for_model(Routine)
event_type = ContentType.objects.get_for_model(Event)
diet_type = ContentType.objects.get_for_model(DietPlan)
inventory_type = ContentType.objects.get_for_model(InventoryItem)

# exercise_manage_permission = Permission.objects.create(codename='can_manage_exercise',
#                                                        name='Can manage Exercise',
#                                                        content_type=exercise_type)
# routine_manage_permission = Permission.objects.create(codename='can_manage_routine',
#                                                       name='Can manage Routine',
#                                                       content_type=routine_type)

# staff_manage_permission = Permission.objects.create(codename='can_manage_staff',
#                                                     name='Can manage Staff',
#                                                     content_type=User)
# inventory_view_permission = Permission.objects.create(codename='can_view_inventory',
#                                                       name='Can view Inventory',
#                                                       content_type=InventoryItem)

# inventory_manage_permission = Permission.objects.create(codename='can_manage_inventory',
#                                                         name='Can manage Inventory',
#                                                         content_type=InventoryItem)
# events_manage_permission = Permission.objects.create(codename='can_manage_events',
#                                                      name='Can manage Events',
#                                                      content_type=Event)
# diets_manage_permission = Permission.objects.create(codename='can_manage_diets',
#                                                     name='Can manage Diets',
#                                                     content_type=DietPlan)

# trainer.permissions.add(exercise_manage_permission)
# trainer.permissions.add(routine_manage_permission)

# economist.permissions.add(staff_manage_permission)
# economist.permissions.add(inventory_view_permission)

# manager.permissions.add(inventory_manage_permission)
# manager.permissions.add(events_manage_permission)
# manager.permissions.add(diets_manage_permission)
