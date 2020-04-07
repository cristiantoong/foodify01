from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes_view, name='recipes_view'),
    path('recipe/<str:pk>/', views.recipe_view, name='recipe_view'),
    path('recipe_user_view/<str:pk>/', views.recipe_user_view, name='recipe_user_view'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('update_recipe/<str:pk>/', views.update_recipe, name='update_recipe'),
    #path('update_recipe_test/<str:pk>/', views.update_recipe_test, name='update_recipe_test'),
    path('delete_recipe/<str:pk>/', views.delete_recipe, name='delete_recipe'),

    
]
