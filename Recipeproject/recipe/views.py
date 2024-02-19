from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def recipe(request):
    if request.method == 'POST':

        data = request.POST
        
        r_name = data.get("recipe_name")
        r_img = request.FILES.get("recipe_img")
        r_desc = data.get("recipe_desc")

        Recipesclass.objects.create(
            recipe_name = r_name,
            recipe_desc = r_desc,
            recipe_img = r_img
        )

        return redirect('/recipe/')
        

    return render(request,'recipe.html')


def showrecipes(request):
    save = Recipesclass.objects.all()

    context = {'querys':save}


    return render(request,'Showrecipe.html',context)

def deleterecipe(request,id):
    rec = Recipesclass.objects.get(id=id)

    rec.delete()
    return redirect('/showrecipe/')

def upddaterecipe(request,id):
    rec = Recipesclass.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        
        r_name = data.get("recipe_name")
        r_img = request.FILES.get("recipe_img")
        r_desc = data.get("recipe_desc")

        rec.recipe_name = r_name
        rec.recipe_desc = r_desc
        
        if r_img:
            rec.recipe_img = r_img

        rec.save()
        return redirect('/showrecipe/')

    context = {'recipe':rec}
    return render(request,'update-recipe.html',context)

