from django.contrib import admin

# Register your models here.

from aclarknet.aclarknet.models import Client

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

