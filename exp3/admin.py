from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import User, Education, Work

admin.site.register(User)
admin.site.register(Education)
admin.site.register(Work)
