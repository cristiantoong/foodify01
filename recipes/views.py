from django.shortcuts import render, redirect, reverse
from .models import Recipe, Comment
from django.shortcuts import get_object_or_404
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import UserProfile





def home(request):
    recipes = Recipe.objects.order_by('-publish_date')

    
    context = {
        'recipes': recipes,
        #'has_profile': has_profile,
        }
    return render(request, 'recipes/index.html', context)


@login_required
def recipes_view(request):
    recipes = Recipe.objects.filter(author=request.user).order_by('-publish_date')
    
    
    context = {
        'recipes': recipes,
        }
    return render(request, 'recipes/recipes_view.html', context)



def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # ingredients = recipe.ingredients
    # instructions = recipe.instructions
    comment_form = CommentForm(request.POST or None)
    user_profile = UserProfile.objects.filter(profile_name=recipe.author)


    comment = Comment.objects.filter(user=recipe.author)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = recipe
            comment_form.save()
            return redirect('recipes:recipe_view', pk=recipe.pk)
    
    context = {
        'recipe': recipe,
        'comment_form': comment_form,
        'user_profile': user_profile,
        #'comment_user_pic': comment_user_pic,
        # 'ingredients': ingredients,
        # 'instructions': instructions,
        }
    return render(request, 'recipes/recipe_view.html', context)
    
@login_required
def recipe_user_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comment_form = CommentForm(request.POST or None)
    # ingredients = recipe.ingredients
    # instructions = recipe.instructions
    
    comment = Comment.objects.filter(user=recipe.author)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = recipe
            comment_form.save()
            return redirect('recipes:recipe_user_view', pk=recipe.pk)

    context = {
        'recipe': recipe,
        'comment_form': comment_form,
        # 'ingredients': ingredients,
        # 'instructions': instructions,
        }
    return render(request, 'recipes/recipe_user_view.html', context)

@login_required
def create_recipe(request):
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()

            messages.success(request, f'Your account has been created! Your are now able to log in')
            return redirect('recipes:recipes_view')
    else:
        form = RecipeForm()
    context = {
        'form':form
    }
    return render(request, 'recipes/create_recipe.html', context)

@login_required
def update_recipe(request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        form = RecipeForm(instance=recipe)

        if request.method == 'POST':
            form = RecipeForm(request.POST or None,  request.FILES or None, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('recipes:recipe_view', pk=recipe.pk)
        
        context = {
            'form': form,
            'recipe': recipe,
            }
        return render(request, 'recipes/update_recipe.html', context)

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:home')
    
    context = {'recipe': recipe}
    return render(request, 'recipes/delete_recipe.html', context)





