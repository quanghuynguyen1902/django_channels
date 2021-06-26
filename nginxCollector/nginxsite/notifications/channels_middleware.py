# from django.db import close_old_connections
# from users.models import User
# from channels.auth import AuthMiddlewareStack

# @database_sync_to_async
# def get_user(app_key):
#     try:
#         user = User.objects.get(app_key=str(app_key))
#         return user
#     except User.DoesNotExist:
#         return AnonymousUser() 
 
# class CustomAuthMiddleware:
#     """
#     Custom token auth middleware
#     """
 
#     def __init__(self, inner):
#         # Store the ASGI application we were passed
#         self.inner = inner
 
#     async def __call__(self, scope, receive, send):
#         scope['user'] = await get_user(scope["query_string"].decode("utf8").split("=")[1])
#         return self.inner(scope, receive, send)

# TokenAuthMiddlewareStack = lambda inner: CustomAuthMiddleware(AuthMiddlewareStack(inner))