from django.urls import path
from myapp import views 


urlpatterns = [path("", views.home, name="home"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path("update/todo/<int:pk>/", views.update_todo, name="update_todo"),
    path("complete/todo/<int:pk>/", views.complete_todo, name="complete_todo"),
    path("delete/todo/<int:pk>/", views.delete_todo, name="delete_todo"),
    
]