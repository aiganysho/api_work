from django.urls import path
from api.views import add_view, get_token_view, subtract_view, multiply_view, divide_view

app_name = 'api'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
]