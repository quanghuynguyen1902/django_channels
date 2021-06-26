from django.urls import include, path
from rest_framework.routers import DefaultRouter
from notifications.api.views import notification_history_views as nv
from notifications.api.views import notification_count_views as ncv

router = DefaultRouter()
router.register(r"notification", nv.NotificationHistoryViewSet)
router.register(r"notification_count", ncv.NotificationCountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('send-notification/', nv.send_notification),
]
