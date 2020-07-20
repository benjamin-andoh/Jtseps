from django.contrib import admin
from users.models import Profile,Branch


#
# class BranchAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'address')


admin.site.register(Branch)


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location', 'address')


admin.site.register(Profile)