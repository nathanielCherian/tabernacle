from django.contrib import admin
from django.urls import path
from .views import home_page, missions_page, about_page
from . import views

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('media/', views.media_page, name='media_page'),
    path('our-story/', views.our_story, name='our_story'),

    path('ministries/', views.ministries_page, name='ministries_page'),
    path('ministries/sunday-school/', views.sunday_school, name='sunday_school'),
    path('ministries/youth/', views.youth, name='youth'),
    path('ministries/literature-ministry/', views.literature_ministry, name='literature_ministry'),
    path('ministries/vbs/', views.vbs, name='vbs'),
    path('ministries/seekers-meeting/', views.seekers_meeting, name='seekers_meeting'),
    path('ministries/evangalism/', views.evangalism, name='evangalism'),
    path('ministries/family-seminar/', views.family_seminar, name='family_seminar'),
    path('ministries/relief-work/', views.relief_work, name='relief_work'),
    path('ministries/christmas/', views.christmas, name='christmas'),


    path('missions/', missions_page, name='missions_page'),
    path('missions/tailoring-center/', views.tailoring_center, name='tailoring_center'),
    path('missions/discipleship-centre/', views.discipleship_centre, name='discipleship_centre'),
    path('missions/free-tuition-center/', views.tuition_center, name='tuition_center'),

]