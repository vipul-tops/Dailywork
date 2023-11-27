from rest_framework import routers
from .views import SubjectViewSet, StaffViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls