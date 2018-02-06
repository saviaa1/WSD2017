"""WSDProject2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from homepage import views as homeviews
from gamelist import views as gamelistviews
from gamepage import views as gamepageviews
from payment import views as paymentviews
from authentication import views as authenticationviews
from django.contrib.auth import views as django_authentication_views
from developer import views as developerviews

urlpatterns = [

    #URLs for authentication part of the site
    path('admin/', admin.site.urls),
    path('', homeviews.index, name='index'),
    path('gamelist/', gamelistviews.GameListView.as_view(), name='gamelist'),
    path('gamepage/<int:gameid>/', gamepageviews.gameviews, name='gamepage'),
    path('payment', paymentviews.payments, name='payment'),
    path('payment/success', paymentviews.success, name='payment/success'),
    path('payment/cancel', paymentviews.cancel, name='payment/cancel'),
    path('payment/error', paymentviews.error, name='payment/error'),
    url(r'^debug/$', authenticationviews.debug, name='debug'),
    url(r'^register/$', authenticationviews.register, name='register'),
    url(r'^login/$', django_authentication_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^account_activation_sent/$', authenticationviews.authEmailSent, name='authEmailSent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        authenticationviews.activate, name='activate'),
    url(r'^logout/$', django_authentication_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^developer/$', authenticationviews.developer, name='developer'),
    path('adding/', developerviews.adding, name='adding'),
]
