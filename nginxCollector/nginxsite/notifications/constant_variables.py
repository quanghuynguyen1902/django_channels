class NotificationStatus:
    READ = 'R'
    UNREAD = 'U'
    NEW = 'N'


class VerboseNotificationStatus:
    READ = 'Read'
    UNREAD = 'Unread'
    NEW = 'New'


class NotificationTitle:
    UPLOAD_DOCUMENT = 'Tải lên tài liệu'


NOTIFICATION_STATUS = [
    (NotificationStatus.NEW, VerboseNotificationStatus.NEW),
    (NotificationStatus.READ, VerboseNotificationStatus.READ),
    (NotificationStatus.UNREAD, VerboseNotificationStatus.UNREAD),
]
