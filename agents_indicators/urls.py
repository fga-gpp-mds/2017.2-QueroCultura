from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='agentes'),
    url(r'^/grafico/(?P<graphic_id>[0-9]+)/$',views.graphic_detail, name='agents_graphic_detail'),
]
