from django.urls import path
from .views import StateMigrationAPIView

urlpatterns = [
    path('previous_state/<str:state>/', StateMigrationAPIView.as_view()),
    path('previous_state/<str:state>/<int:year>/', StateMigrationAPIView.as_view()),
    path('previous_division/<str:div>/', StateMigrationAPIView.as_view()),
    path('previous_division/<str:div>/<int:year>/', StateMigrationAPIView.as_view())
]
