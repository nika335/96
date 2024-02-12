from django.shortcuts import render, redirect
from .models import Recipe


def index(request):
    recipe = Recipe.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        return redirect('edit', name)
    return render(request,'index.html', {'recipe':recipe})


def wiev_recepies(request, name):
    recipe = Recipe.objects.get(name=name)
    return render(request, 'wiev_recepies.html', {'recipe':recipe})


def add_recipe(request):
    if request.method == 'POST':
        new_recipe = Recipe(
            name = request.POST.get('name'),
            ingredients = request.POST.get('ingredients'),
            instructions = request.POST.get('instructions'),
        )
        new_recipe.save()
        return redirect('index')
    return render(request, 'add_recepie.html')


def edit_recepue(request, name):
    recipe = Recipe.objects.get(name=name)
    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions')
        recipe.save()
        return redirect('index')
    return render(request, 'edit_recepue.html', {'recope':recipe})
