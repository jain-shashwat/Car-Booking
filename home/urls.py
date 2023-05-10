from django.urls import path,include
from . import views
app_name='home'
urlpatterns = [

    # path('', views.home,name='home'),
    path('',views.Home.as_view(),name='index'),
    # path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('<int:pk>/',views.detail,name='detail'),
    path('booking/<int:id>/', views.booking, name='booking'),
    path('checkout/<visitor_name>/<phone_number>/<platinum_seats>/<gold_seats>/<silver_seats>/<total_platinum_price>/<total_gold_price>/<total_silver_price>/<net_price>/<booked_date>/',views.checkout,name='checkout'),
    path('search/',views.search,name='search'),
    path('check_avai/<int:id>/',views.check_avai,name='check_avai')

]
