from django.urls import path, include
from rest_framework import routers

from .views import ExpenseAPIView, OwnExpenseAPIView


router = routers.SimpleRouter()
router.register('expense', ExpenseAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('own-expenses/', OwnExpenseAPIView.as_view())
]
