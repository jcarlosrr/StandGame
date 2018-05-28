from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from soporte import views


from soporte.views import (
    JuegoList,
    JuegoDetail,
    JuegoCreation,
    JuegoUpdate,
    JuegoDelete
)

urlpatterns = [
	#url(r'^$', index, name='index'),
    url(r'^$', JuegoList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', JuegoDetail.as_view(), name='detail'),
    url(r'^nuevo$', JuegoCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', JuegoUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', JuegoDelete.as_view(), name='delete'),
    url(r'^buscar/$', views.search, name='buscar'),
]