"""bookswap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
 
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from bookswap.offer.views import OfferViewSet,OfferSearchList
from bookswap.user_profile.views import UserViewSet,UserProfileViewSet,GlobalSearchList
from bookswap.author.views import AuthorViewSet
router = routers.DefaultRouter()
router.register(r'offers', OfferViewSet)
router.register(r'authors', AuthorViewSet) 
router.register(r'users', UserViewSet) 
router.register(r'user_profiles', UserProfileViewSet) 


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user_search/$', GlobalSearchList.as_view(), name="search_user"),
    url(r'^offer_search/$', OfferSearchList.as_view(), name="search_offer"),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
