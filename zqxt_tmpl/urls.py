"""zqxt_tmpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^add/$',learn_views.add,name='add'),
    url(r'^statues/$',learn_views.statues,name='statues'),
    url(r'^home/$',learn_views.home,name='home'),
    url(r'^display/$',learn_views.display,name='display'),
    url(r'^peoplenum/$',learn_views.peoplenum,name='peoplenum'),
    url(r'^admin/', admin.site.urls),
    url(r'^return_peoplenum/$', learn_views.return_peoplenum,name='return_peoplenum'),
]
