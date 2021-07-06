from rest_framework.routers import DefaultRouter
from apirest.api.vuelos_views import VueloSViewSet
from apirest.api.reporte_views import ReporteViewSet

router = DefaultRouter()

router.register(r'vuelos', VueloSViewSet)

router.register(r'reporte',ReporteViewSet) 


urlpatterns = router.urls
