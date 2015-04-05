from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomeView

urlpatterns = [
    # Examples:
    # url(r'^$', 'home.views.HomeView', name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^home/', include('home.urls')),

    url(r'^admin/', include(admin.site.urls))
]
