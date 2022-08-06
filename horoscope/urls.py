from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('types', views.types, name='horoscope-types'),
    path('types/<str:sign_type>', views.get_info_about_types, name='type-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
