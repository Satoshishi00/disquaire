from django.urls import path, re_path

from . import views  # import views so we can use them in urls.

urlpatterns = [
    # "/store" will call the method "index" in "views.py"
    re_path(r'^$', views.listing, name="listing"),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    re_path(r'^search/$', views.search, name="search"),
]

app_name = 'store'