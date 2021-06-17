from rest_framework.routers import DefaultRouter
from apirest.api.vuelos_views import VueloSViewSet


router = DefaultRouter()

router.register(r'vuelos', VueloSViewSet)

urlpatterns = router.urls
