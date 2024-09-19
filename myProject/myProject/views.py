from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def loginPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login(req,user)
            return redirect('homePage')
        
    return render(req,'loginPage.html')

def signupPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')

        if password == confirm_password:
            user=CustomUser.objects.create_user(
                username=username,
                email=email,
                usertype=usertype,
                password=password
            )
            return redirect('loginPage')

    return render(req,'signupPage.html')

def logoutPage(req):
    logout(req)
    return redirect('loginPage')

@login_required
def homePage(req):
    return render(req,'homePage.html')

def addresume(req):
    All_User=CustomUser.objects.all()
    if req.method == 'POST':
        
        Designation=req.POST.get('Designation')
        Contact_number=req.POST.get('Contact_number')
        Career_Summary=req.POST.get('Career_Summary')
        Experience_Title=req.POST.get('Experience_Title')
        Skill_title=req.POST.get('Skill_title')
        Education_Title=req.POST.get('Education_Title')
        Language=req.POST.get('Language')
        Interest=req.POST.get('Interest')
        Profile_Pic=req.FILES.get('Profile_Pic')
        Linkedin_URL=req.POST.get('Linkedin_URL')
        Facebook_URL=req.POST.get('Facebook_URL')
        Instagram_URL=req.POST.get('Instagram_URL')
        GitHub_URL=req.POST.get('GitHub_URL')

        customuser_id=req.POST.get('customuser_id')
       
        user_object=get_object_or_404(CustomUser,id=customuser_id)

        resume=ResumeModel(
            
            user=user_object,
            Designation=Designation,
            Contact_number=Contact_number,
            Career_Summary=Career_Summary,
            Experience_Title=Experience_Title,
            Skill_title=Skill_title,
            Education_Title=Education_Title,
            Language=Language,
            Interest=Interest,
            Profile_Pic=Profile_Pic,
            Linkedin_URL=Linkedin_URL,
            Facebook_URL=Facebook_URL,
            Instagram_URL=Instagram_URL,
            GitHub_URL=GitHub_URL,
        )
        resume.save()
        return redirect('resumelist')
    
    
    return render(req,'addresume.html',{'All_User':All_User})

def resumelist(req):
    resume=ResumeModel.objects.all()
    Education=Education_model.objects.all()
    Interest=interest_model.objects.all()
    Skill=Skill_model.objects.all()

    context={
        'resume':resume,
        'Education':Education,
        'Interest':Interest,
        'Skill':Skill,
    }
    return render(req,'resumelist.html',context)

def deletePage(req,id):
    data=CustomUser.objects.filter(id=id)
    data.delete()
    return redirect('resumelist')

def viewResume(req,myid):
    my_user=CustomUser.objects.get(id=myid)

    context={
        'resumes':ResumeModel.objects.filter(user=my_user),
        'my_user':my_user,
        'Education':Education_model.objects.filter(user=my_user),
        'Interest':interest_model.objects.filter(user=my_user),
        'Skill':Skill_model.objects.filter(user=my_user),
        'Experience':Experience_model.objects.filter(user=my_user),
        'language':language_model.objects.filter(user=my_user),
    }
    return render(req,'viewResume.html',context)

def addSkill(req):

    All_User=CustomUser.objects.all()
    All_Skills=intermidiate_skill_Model.objects.all()
    
    if req.method == 'POST':
        
        customuser_id=req.POST.get('customuser_id')
        skill_id=req.POST.get('skill_id')
        
        skill_name=get_object_or_404(intermidiate_skill_Model,id=skill_id)
        profecency_level=req.POST.get('profecency_level')
       

        user_object=get_object_or_404(CustomUser,id=customuser_id)

        resume=Skill_model(
            
            user=user_object,
            skill_name=skill_name,
            profecency_level=profecency_level,
        )
        resume.save()
        return redirect('viewSkill')
    
    return render(req,'addSkill.html',{'All_User':All_User,'All_Skills':All_Skills})

def addEducation(req):
    All_User=CustomUser.objects.all()
    
    if req.method == 'POST':
        
        customuser_id=req.POST.get('customuser_id')
        
        title=req.POST.get('title')
        start_date=req.POST.get('start_date')
        end_date=req.POST.get('profecency_level')
       

       
        user_object=get_object_or_404(CustomUser,id=customuser_id)

        resume=Education_model(
            
            user=user_object,
            title=title,
            start_date=start_date,
            end_date=end_date,
        )
        resume.save()
        return redirect('viewEducation')
    
    
    return render(req,'addEducation.html',{'All_User':All_User})

def addExperience(req):
    All_User=CustomUser.objects.all()
    
    if req.method == 'POST':
        
        customuser_id=req.POST.get('customuser_id')
        
        title=req.POST.get('title')
        start_date=req.POST.get('start_date')
        end_date=req.POST.get('profecency_level')
       

       
        user_object=get_object_or_404(CustomUser,id=customuser_id)

        resume=Experience_model(
            
            user=user_object,
            title=title,
            start_date=start_date,
            end_date=end_date,
        )
        resume.save()
        return redirect('viewExperience')
    
    return render(req,'addExperience.html',{'All_User':All_User})

def addInterest(req):
    All_User=CustomUser.objects.all()
    All_interests=intermidiate_interest_model.objects.all()
    
    if req.method == 'POST':
        
        customuser_id=req.POST.get('customuser_id')
        interest_name=get_object_or_404(intermidiate_interest_model,id=interest_id)
        
        interest_name=req.POST.get('interest_name')
       
        user_object=get_object_or_404(CustomUser,id=customuser_id)
        interest_id=req.POST.get('interest_id')

        resume=interest_model(
            
            user=user_object,
            interest_name=interest_name,
        )
        resume.save()
        return redirect('viewInterest')
    
    return render(req,'addInterest.html',{'All_User':All_User,'All_interests':All_interests})

def addLanguage(req):
   All_User=CustomUser.objects.all()
    
   if req.method == 'POST':
        
        customuser_id=req.POST.get('customuser_id')
        
        language_name=req.POST.get('language_name')
        profecency_level=req.POST.get('profecency_level')
       

       
        user_object=get_object_or_404(CustomUser,id=customuser_id)

        resume=language_model(
            
            user=user_object,
            language_name=language_name,
            profecency_level=profecency_level,
        )
        resume.save()
        return redirect('viewLanguage')
    
   return render(req,'addLanguage.html',{'All_User':All_User})



def viewSkill(req):
    resume=Skill_model.objects.all()
    context={
        'resume':resume
    }
    return render(req,'viewSkill.html',context)

def viewEducation(req):
    resume=Education_model.objects.all()
    context={
        'resume':resume
    }
    return render(req,'viewEducation.html',context)

def viewExperience(req):
    resume=Experience_model.objects.all()
    context={
        'resume':resume
    }
    return render(req,'viewExperience.html',context)

def viewInterest(req):
    resume=interest_model.objects.all()
    context={
        'resume':resume
    }
    return render(req,'viewInterest.html',context)

def viewLanguage(req):
    resume=language_model.objects.all()
    context={
        'resume':resume
    }
    return render(req,'viewLanguage.html',context)