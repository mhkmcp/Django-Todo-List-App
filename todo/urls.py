from django.urls import path
from . import views as v

# app_name = 'todo'

urlpatterns = [
    path('', v.index, name='index'),
    path('add', v.add_todo, name='add'),
    path('complete/<todo_id>', v.complete_todo, name='complete'),
    path('deletecomplete', v.delete_completed, name='deletecomplete'),
    path('deleteall', v.delete_all, name='deleteall')

]
