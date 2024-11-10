from django.shortcuts import render
from django.views.generic import ListView

from fruits.models import Fruit
from profiles.models import Profile


# Create your views here.


def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }

    return render(request, 'common/index.html', context)


class Dashboard(ListView):
    template_name = 'common/dashboard.html'
    model = Fruit

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context