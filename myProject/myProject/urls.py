from myProject.views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage,name='loginPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('homePage/',homePage,name='homePage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('addresume/',addresume,name='addresume'),
    path('resumelist/',resumelist,name='resumelist'),
    path('deletePage/<int:id>',deletePage,name='deletePage'),
    path('viewResume/<int:myid>',viewResume,name='viewResume'),
    path('addSkill/',addSkill,name='addSkill'),
    path('addEducation/',addEducation,name='addEducation'),
    path('addExperience/',addExperience,name='addExperience'),
    path('addInterest/',addInterest,name='addInterest'),
    path('addLanguage/',addLanguage,name='addLanguage'),
    path('viewSkill/',viewSkill,name='viewSkill'),
    path('viewEducation/',viewEducation,name='viewEducation'),
    path('viewExperience/',viewExperience,name='viewExperience'),
    path('viewInterest/',viewInterest,name='viewInterest'),
    path('viewLanguage/',viewLanguage,name='viewLanguage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
