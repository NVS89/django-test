from django.urls import path

from .views import index, details

app_name = 'pages'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', details, name='details')
]
