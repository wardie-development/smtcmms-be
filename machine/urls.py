from utils import router

from .views import MachineViewSet, ManufacturerViewSet, MachineTypeViewSet

app_name = "apps.machine"

router.register("machine", MachineViewSet, basename="machine")
router.register("manufacturer", ManufacturerViewSet, basename="manufacturer")
router.register("machinetype", MachineTypeViewSet, basename="machinetype")
