from django.urls import path, include
from . import views

urlpatterns = [

   path('index',views.index,name='index'),
   
   path('about',views.about,name='about'),
    path('python',views.python,name='python'),
    path('sql',views.sql,name='sql'),
    path('excel',views.excel,name='excel'),
    path('powerbi',views.powerbi,name='powerbi'),
    path('tableau',views.tableau,name='tableau'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact')
]
