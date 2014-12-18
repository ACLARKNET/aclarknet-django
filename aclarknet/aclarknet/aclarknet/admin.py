from aclarknet.aclarknet.models import Client
from aclarknet.aclarknet.models import Service
from aclarknet.aclarknet.models import TeamMember
from django.contrib import admin


class ClientAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


class TeamMemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
