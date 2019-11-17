from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.home_page,name = 'home_page'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^search/', views.search, name='search'),
    url(r'^comment/(?P<image_id>\d+)', views.one_image, name='comment'),
]

