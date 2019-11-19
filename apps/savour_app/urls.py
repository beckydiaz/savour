from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^savour/dashboard$', views.savour_dashboard),
# url(r'^trip/new$', views.trip_new),
# url(r'^trip/create$', views.trip_create),
# url(r'^trip/(?P<trip_id>\d+)$', views.trip_view),
# url(r'^trip/edit/(?P<trip_id>\d+)$', views.trip_edit),
# url(r'^trip/update/(?P<trip_id>\d+)$', views.trip_update),
# url(r'^trip/remove/(?P<trip_id>\d+)$', views.trip_remove),

]