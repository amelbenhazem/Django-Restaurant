from rest_framework.routers import DefaultRouter
from .api_views import RestaurantViewSet, TableViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls
