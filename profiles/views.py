from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile
from django.urls import reverse_lazy


class CreateProfile(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')


def details_profile(request):
    profile = Profile.objects.first()
    posts = profile.fruit_set.all().count()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'profiles/details-profile.html', context)


class EditProfile(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self,queryset=None):
        return Profile.objects.first()


def delete_profile(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    return render(request, 'profiles/delete-profile.html', context)
