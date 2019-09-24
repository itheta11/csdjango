from rest_framework_mongoengine import routers
from crmsystem.views import EmployeeView

router = routers.DefaultRouter()
router.register(r'crmsystem', EmployeeView)

urlpatterns = []
urlpatterns += router.urls