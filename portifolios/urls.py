from django.conf.urls import url
from . import views 

app_name = "portifolio"

urlpatterns = [
    url(r'^$', views.portifolio_exibir),
]