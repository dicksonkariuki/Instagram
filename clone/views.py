from django.shortcuts import render,redirect,get_object_or_404
from .models import Comment,Image,Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from.forms import ProfileForm,ImageForm,CommentForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def profile(request, username):
    uploadform= ImageForm
    image = Image.objects.all()
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'main_pages/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images,'uploadform':uploadform,'image':image})
    '''
    editing user profile fillform & submission
    '''
@login_required(login_url='/accounts/login/')
def home_page(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{'image':image})
@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'main_pages/edit_profile.html', {'form':form})
    '''
    logs out current user from account

# Create your views here.
