from django.contrib import admin
from django.urls import path, include
from registration_app.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('accounts/', include('registration_app.urls')),
]