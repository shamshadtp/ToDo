from rest_framework.routers import DefaultRouter
from api.views import TaskViewset
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path
router=DefaultRouter()
router.register("v2/task",TaskViewset,basename="task")


urlpatterns=[
    path("token",ObtainAuthToken.as_view())
]+router.urls