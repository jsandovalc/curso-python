from django.urls import path
from .views import BillItemCreate


urlpatterns = [
    path("bill/new", BillItemCreate.as_view(), name="testbill_new")
]
