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
from api import views as apiviews

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', homeviews.index, name='index'),
    path('gamelist/', gamelistviews.GameListView.as_view(), name='gamelist'),
    path('gamelist/<category>/', gamelistviews.GameListView.as_view(), name='gamelist'),
    path('gamepage/<int:gameid>/', gamepageviews.gameviews, name='gamepage'),
    path('gamepage/<int:gameid>/loadgamedata/', gamepageviews.loadgamedata, name='loadgamedata'),
    path('purchase/<int:gameid>/', paymentviews.payments, name='purchase'),
    path('purchase/success/', paymentviews.success, name='purchase/success'),
    path('purchase/cancel/', paymentviews.cancel, name='purchase/cancel'),
    path('purchase/error/', paymentviews.error, name='purchase/error'),
    path('emailsuccess/', authenticationviews.emailsuccess, name='emailsuccess'),
    path('register/', authenticationviews.register, name='register'),
    path('login/', django_authentication_views.login, {'template_name': 'login.html'}, name='login'),
    path('account_activation_sent/', authenticationviews.authEmailSent, name='authEmailSent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        authenticationviews.activate, name='activate'),
    path('logout/', django_authentication_views.logout, {'next_page': 'login'}, name='logout'),
    path('developer/', authenticationviews.developer, name='developer'),
    path('adding/', developerviews.adding, name='adding'),
    url(r'^(?P<object_id>[0-9]+)/delete_game/$', developerviews.deleting, name='delete_game'),
    path('profile/', developerviews.profile, name='profile'),
    url(r'^(?P<object_id>[0-9]+)/edit_game/$', developerviews.editing, name='edit_game'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('profile/password/', developerviews.password, name='password'),
    url(r'^profile/(?P<object_id>[0-9]+)/$', developerviews.statistics, name='statistics'),
    path('api/games/', apiviews.games, name='games'),
    url(r'^api/highscores/$', apiviews.highscores, name='highscores'),
    url(r'^api/highscores/(?P<object_id>[0-9]+)/$', apiviews.highscoresPerGame, name='highscoresPerGame'),
    url(r'^api/sales/(?P<object_id>[0-9]+)/$', apiviews.saleStatistics, name='saleStatistics'),
]
