from rest_framework.routers import DefaultRouter
from reserve.api.view_sets import *

router = DefaultRouter()
router.register('reserve', ReserveViewSet, basename='reserve')

urlpatterns = router.urls
