from django.urls  import path
from . import views
from report.views import index

urlpatterns = [
    # path('report/', views.report, name='report'),
    path('', index),
]
