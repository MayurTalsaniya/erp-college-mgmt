# from django.contrib import admin

# # Register your models here.
# from django.contrib.auth.admin import UserAdmin

# from student_management_app.models import CustomUser

# class UserModel(UserAdmin):
#     pass

# admin.site.register(CustomUser,UserModel)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # This makes sure required fields are displayed in the admin
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_superuser']
    list_filter = ['user_type', 'is_staff', 'is_superuser']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
