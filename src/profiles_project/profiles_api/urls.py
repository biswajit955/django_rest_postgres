from django.urls import include, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile-singup', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    re_path('hello-view/', views.HelloApiView.as_view()),
    re_path('', include(router.urls)),
]
