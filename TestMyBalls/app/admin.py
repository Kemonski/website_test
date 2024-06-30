from django.contrib import admin
from .models import Games, Profile, Client, Payment, Report, UsagiInfo

admin.site.register(Games)
admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Report)
admin.site.register(UsagiInfo)
