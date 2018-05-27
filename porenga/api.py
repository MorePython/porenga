from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



_urls = [
    path('token/', obtain_jwt_token, name='get-token'),
    path('token/refresh', refresh_jwt_token, name='refresh-token'),
    path('token/verify', verify_jwt_token, name='verify-token')
]

urls = (_urls, 'api.v1', 'api.v1')

