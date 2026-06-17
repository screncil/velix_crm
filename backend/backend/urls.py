
from django.contrib import admin
from django.urls import path, include

from users.views import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from client.views import AllWhereKnow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include("users.urls"), name="users"),
    path('api/sinotracks/', include("sinotrack.urls"), name="sinotracks"),
    path('api/bikes/', include('bike.urls'), name="bikes"),
    path('api/clients/', include('client.urls'), name="client"),
    path('api/whereknow/all', AllWhereKnow.as_view()),
    path('api/category/', include("item_categories.urls"))
]
