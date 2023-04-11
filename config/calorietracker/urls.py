from django.urls import path
from .views import FoodItemCreateView, FoodItemListView, SelectFoodCreateView, DeleteFoodView, ProfileView, EditCalorielimitView , UserInfo
# from accounts.views import Profile
urlpatterns = [
    path('', ProfileView,name='profile'),
    path('fooditem_create/', FoodItemCreateView.as_view(), name='fooditem_create'),
    path('fooditem_list/', FoodItemListView.as_view(), name='fooditem_list'),
#     path('fooditem_delete/<int:pk>',
#          FoodItemDeleteView.as_view(), name='fooditem_delete'),
    path('selectfooditem/', SelectFoodCreateView, name='selectfooditem'),
    path('deleteselectedfood/<int:pk>',
         DeleteFoodView.as_view(), name='deleteselectedfood'),
    path('profile/', ProfileView, name='profile'),
    path('calorielimit_edit/<int:pk>',
         EditCalorielimitView.as_view(), name='calorielimit_edit'),
    path('userinfo', UserInfo.as_view() ,name='userinfo'),
 ]
