from django.urls  import path
from . import views

urlpatterns = [
    # path('report/', views.report, name='report'),
    path('', views.index, name='index'),
]
