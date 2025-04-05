from django.shortcuts import render,redirect
from users.models import Profiles,Skills,Message
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.db.models import Q
from .utils import searchProfiles,paginateProfiles

# Create your views here.
def profiles(request):
   profiles, search_query = searchProfiles(request)
   results = 4
   custom_range,profiles = paginateProfiles(request,profiles,results)
   context = {"profiles": profiles,"search_query":search_query,"custom_range":custom_range}

   return render(request, 'users/profiles.html', context)

def user_profile(request,pk):
   profile = Profiles.objects.get(id = pk)
   top_skills = profile.skills_set.exclude(description__exact = "")
   other_skills = profile.skills_set.filter(description = "")
   context = {"profile":profile,"top_skills":top_skills,"other_skills":other_skills}
   return render(request, 'users/user-profile.html',context)

def loginUser(request):
   page = "login"
   if request.user.is_authenticated:
      return redirect('profiles')
   if request.method == "POST":
      username = request.POST['username'].lower()
      password = request.POST['password']
      try:
         user = User.objects.get(username = username)
      except:
         messages.error(request, 'Username doesnot exist')
      user = authenticate(request, username = username, password = password)
      if user is not None:
         login(request,user)
         return redirect(request.GET['next'] if 'next' in request.GET else 'account')
      else:
         messages.error(request,"Username or password does not exists")
   return render(request, 'users/login_register.html')
def logoutUser(request):
   logout(request)
   messages.success(request,"User logged out successfully")
   return redirect('login')

def registerUser(request):
   page = "register"
   form = CustomUserCreationForm()
   if request.method == "POST":
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.username = user.username.lower()
         user.save()  
         messages.info(request,"Registerd Successfully")
         login(request,user)
         return redirect('edit-account')
      else:
         messages.error(request, "Error occured while registration")
   context = {"page" : page, "form" : form}
   return render(request, 'users/login_register.html',context)

@login_required(login_url = 'login')
def userAccount(request):
   profile = request.user.profiles
   skills = profile.skills_set.all()
   projects = profile.projects_set.all()
   context = {"profile":profile,"skills":skills,"projects":projects}
   return render(request,'users/account.html',context)

@login_required(login_url = 'login')
def editAccount(request):
   profile = request.user.profiles
   form = ProfileForm(instance = profile)
   if request.method == "POST":
      form = ProfileForm(request.POST,request.FILES,instance = profile)
      if form.is_valid():
            form.save()
            return redirect('account')
   context = {"form":form}
   return render(request,'users/edit_account.html',context)

@login_required(login_url = 'login')
def addSkill(request):
   profile = request.user.profiles
   form = SkillForm()
   if  request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit = False)
            skill.owner = profile
            skill.save()
            messages.success(request,"Skill added successfully")
            return redirect('account')           

   context = {"form":form}
   return render(request,'users/add_skill.html',context)

@login_required(login_url = 'login')
def updateSkill(request,pk):
   profile = request.user.profiles
   skill = profile.skills_set.get(id = pk)
   form = SkillForm(instance = skill)
   if request.method == "POST":
      form = SkillForm(request.POST,instance = skill)
      if form.is_valid():
         form.save()
         messages.success(request,"Skill updated successfully")
         return redirect('account')
   context = {"form":form}
   return render(request,'users/add_skill.html',context)

@login_required(login_url = 'login')
def deleteSkill(request,pk):
   profile = request.user.profiles
   skill = profile.skills_set.get(id = pk)
   if request.method == "POST":
      skill.delete()
      messages.success(request,"Skill deleted successfully")
      return redirect('account')
   context = {'object':skill}
   return render(request, 'delete_template.html',context)

@login_required(login_url = 'login')
def inbox(request):
   profile = request.user.profiles
   messagesRequests = profile.messagesRequests.all()
   unreadCount = messagesRequests.filter(is_read = False).count()
   context = {'messagesRequests':messagesRequests,'unreadCount':unreadCount}
   return render(request,'users/inbox.html',context)

@login_required(login_url = 'login')
def viewMessage(request,pk):
   profile = request.user.profiles
   message_view = profile.messagesRequests.get(id = pk)
   if message_view.is_read == False:
      message_view.is_read = True
      message_view.save()
   context = {'message_view':message_view}
   return render(request,'users/message.html',context)



   
