from django.contrib import admin

# Register your models here.
from notifications.models.notification_history import NotificationHistory
from notifications.models.notification_count import NotificationCount


# admin.site.register(Template)

# Define the admin class

class CustomNotificationHistoryAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'status', 'last_read', 'created_at')
    list_filter = ('to_user',)

    search_fields = ('to_user',)
    readonly_fields = ()

    filter_horizontal = ()
    fieldsets = ()


class CustomNotificationCountAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity')
    list_filter = ('user', 'quantity')

    search_fields = ('user', 'quantity')
    readonly_fields = ()

    filter_horizontal = ()
    fieldsets = ()


# # Register the admin class with the associated model
admin.site.register(NotificationHistory, CustomNotificationHistoryAdmin)
admin.site.register(NotificationCount, CustomNotificationCountAdmin)
