from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),

    path('complete_task/<int:id>',complete_task,name='complete_task'),
    path('trash_task/<int:id>',trash_task,name='trash_task'),
    path('delete_task/<int:id>',delete_task,name='delete_task'),
    path('delete/<int:id>',delete,name='delete'),
    path('update/<int:id>',update,name='update'),



    path('complete_all/',complete_all,name='complete_all'),
    path('delete_all',delete_all,name='delete_all'),
    path('complete_del/',complete_del,name='complete_del'),
    path('trash_del/',trash_del,name='trash_del'),

    path('restore/<int:id>',restore,name='restore'),
    path('restore_all',restore_all,name='restore_all')

]