from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Feedback)
admin.site.register(EventFeedback)