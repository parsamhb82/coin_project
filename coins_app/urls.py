from django.urls import path
from .views import get_coins_price, get_coins_latest_change

urlpatterns = [
    path('price/<str:src_currency>/<str:dst_currency>/', get_coins_price),
    path('latest/<str:src_currency>/', get_coins_latest_change),
]