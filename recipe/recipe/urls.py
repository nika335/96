
from django.contrib import admin
from django.urls import path
from recipe_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('wiev_recepies/<str:name>', views.wiev_recepies, name='wiev_recepies'),
    path('add_recepie', views.add_recipe, name='add'),
    path('edit_recepue/<str:name>', views.edit_recepue, name='edit'),

]
