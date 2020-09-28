from django.contrib import admin

# Register your models here.
from .models import User,Device,Controller,Sound,Company,GameTitle

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Controller)
admin.site.register(Sound)
admin.site.register(Company)
admin.site.register(GameTitle)