"""voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from .views import ElectionList, CreateElection, MainPage, ElectionDetail, ThanksPage, Results
from django.contrib import admin


urlpatterns = [
   url(r'^election/$', ElectionList.as_view(), name='election-name'),
   url(r'^create-election/$', CreateElection.as_view(), name='create-election'),
   url(r'^home/', MainPage.as_view(), name='main_page'),  #Home page for loged in student
   url(r'^election/(?P<pk>\d+)$', ElectionDetail.as_view(), name='election-detail'),
   url(r'^success/$', ThanksPage.as_view(), name='success-vote'),
   url(r'^results/', Results.as_view(), name='results')
]
