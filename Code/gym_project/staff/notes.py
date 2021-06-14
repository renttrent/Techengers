from staff.models import AdminNotes
from django.utils import timezone


def getNotes():
    notes = 'No notes posted'
    if AdminNotes.objects.first():
        nr = len(AdminNotes.objects.all())
        notes = AdminNotes.objects.all()[nr-1]

        if notes.date < timezone.now():
            return notes
