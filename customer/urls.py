from utils import router

from .views import CustomerViewSet

app_name = "apps.customer"

router.register("customer", CustomerViewSet, basename="customer")
