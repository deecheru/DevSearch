from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projects,Tag
from .forms import *
from django.contrib.auth.decorators import login_required
from .utils import *


def projects(request): 
    projects, search_query = searchProjects(request)    
    results = 3
    custom_range,projects = paginateProjects(request,projects,results)
    context = {'projects': projects,"search_query":search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def project(request, pk):
    projectObj = Projects.objects.get(id = pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit = False)
        review.project = projectObj
        review.owner = request.user.profiles
        review.save()

        projectObj.getVoteCount

        return redirect('project',pk=projectObj.id)

    context = {'project':projectObj,'form':form}
    return render(request,'projects/single_project.html',context)

@login_required(login_url = "login")
def createProject(request):
    profile = request.user.profiles
    form = ProjectForm()
    if  request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url = "login")
def updateProject(request,pk):
    profile = request.user.profiles
    project = profile.projects_set.get(id = pk)
    form = ProjectForm(instance = project)
    if  request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance = project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url = "login")
def deleteProject(request,pk):
    profile = request.user.profiles
    project = profile.projects_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object':project}
    return render(request, 'delete_template.html',context)







# Create your views here.
