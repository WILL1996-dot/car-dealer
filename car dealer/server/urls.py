from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from frontend.views import DealerViewSet, ReviewViewSet, LoginView, LogoutView

router = DefaultRouter()
router.register(r'dealers', DealerViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]