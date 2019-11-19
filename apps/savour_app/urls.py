from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^savour/dashboard$', views.savour_dashboard),
url(r'^savour/recipes$', views.savour_recipes),
url(r'^savour/favorites$', views.savour_favorites),
url(r'^savour/list$', views.savour_list),
url(r'^savour/pantry$', views.savour_pantry)
]