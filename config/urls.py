from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , include('home.urls')),
    path('todos/' , include('todo.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth-token/', obtain_auth_token, name= 'generate_auth_token'),

]
