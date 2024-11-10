from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from fruits.forms import CreateFruitForm, DeleteFruitForm
from fruits.models import Fruit
from django.urls import reverse_lazy

from profiles.models import Profile


class CreateFruit(CreateView):
    model = Fruit
    form_class = CreateFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class EditFruit(UpdateView):
    model = Fruit
    form_class = CreateFruitForm
    pk_url_kwarg = 'id'
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


def delete_fruit(request, id):
    fruit = Fruit.objects.get(pk=id)
    profile = Profile.objects.first()
    form = DeleteFruitForm(instance=fruit)

    context = {
        'fruit': fruit,
        'profile': profile,
        'form': form
    }

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    return render(request, 'fruits/delete-fruit.html', context)


def details_fruit(request, id):
    fruit = Fruit.objects.get(pk=id)
    profile = Profile.objects.first()

    context = {
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, 'fruits/details-fruit.html', context)