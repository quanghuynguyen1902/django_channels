from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_admin', 'email', 'created_at')
    list_filter = ('is_admin', 'is_moderator', 'is_staff')

    search_fields = ('email', 'username')
    readonly_fields = ('created_at', 'last_login')

    filter_horizontal = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)