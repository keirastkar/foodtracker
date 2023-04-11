from .forms import *
from django.urls import reverse_lazy, reverse
from .models import *
from accounts.models import CustomUser
from django.views import generic
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





class FoodItemCreateView(LoginRequiredMixin, CreateView):
    model = Fooditem
    form_class = fooditemcreate
    template_name = 'fooditem_create.html'
    success_url = reverse_lazy('fooditem_list')
    

class FoodItemListView(LoginRequiredMixin, ListView):
    model = Fooditem
    template_name = 'fooditem_list.html'
    fields = "__all__"
    context_object_name = 'fooditems'

class UserInfo(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'userinfo.html'
    


# class FoodItemDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Fooditem
#     template_name = 'fooditem_delete.html'
#     success_url = reverse_lazy('fooditem_list.html')


@login_required(login_url='login')
def SelectFoodCreateView(request):
    usernow = CustomUser.objects.get(id=request.user.id)
    form = selectfoodForm(request.user, instance=usernow)
    FoodList = Fooditem.objects.filter(person=request.user)
    if FoodList.count() == 0:
        f1 =Fooditem(name='grilled chicken(100gr)',
                      calorie=239,carbs=0,protein=27,fat=14, person=request.user)
        f1.save()
        f1 =Fooditem(name='grilled salmon(100gr)',
                      calorie=208,carbs=0,protein=20,fat=13, person=request.user)
        f1.save()
        f1 =Fooditem(name='rice(100gr)',
                      calorie=130,carbs=28,protein=2.7,fat=0.3, person=request.user)
        f1.save()
        f1 =Fooditem(name='white bread(100gr)',
                      calorie=265,carbs=49,protein=9,fat=3.2, person=request.user)
        f1.save()
        f1 =Fooditem(name='egg(100gr)',
                      calorie=155,carbs=1.1,protein=21,fat=11, person=request.user)
        f1.save()
        f1 =Fooditem(name='milk(100gr)',
                      calorie=42,carbs=5,protein=3.4,fat=1, person=request.user)
        f1.save()
        f1 =Fooditem(name='feta cheese(100gr)',
                      calorie=246,carbs=4.1,protein=14,fat=21, person=request.user)
        f1.save()
        f1 =Fooditem(name='date(100gr)',
                      calorie=282,carbs=75,protein=2.5,fat=0.4, person=request.user)
        f1.save()
        f1 =Fooditem(name='meat(100gr)',
                      calorie=143,carbs=0,protein=26,fat=3.5, person=request.user)
        f1.save()
        f1 =Fooditem(name='yogurt(100gr)',
                      calorie=59,carbs=3.6,protein=10,fat=0.4, person=request.user)
        f1.save()

        return redirect('/manage/selectfooditem')
    context = {
        'FoodList': FoodList,
    }
    if request.method == "POST":
        form = selectfoodForm(request.user, request.POST, instance=usernow)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            category = form.cleaned_data.get('category')
            quantity = form.cleaned_data.get('quantity')
            person = form.cleaned_data.get('person')
            selectedfood = Selectfooditem.objects.create(
                name=name, quantity=quantity, category=category, person=person)
            selectedfood.save()
            return redirect('/manage/profile')
        else:
            form = selectfoodForm(request.user)
    context = {'form': form}
    return render(request, 'selectfooditem.html', context)


@login_required(login_url='login')
def ProfileView(request):
    usernow = CustomUser.objects.get(id=request.user.id)
    calorielimit = usernow.calorielimit
    selectedfood = Selectfooditem.objects.filter(person=request.user)

    calorieconsumed = 0
    calorieleft = calorielimit

    for food in selectedfood:
        calorieconsumed += (food.name.calorie * food.quantity)
        calorieleft = calorielimit - calorieconsumed

    context = {'selectedfood': selectedfood, 'Calorielimit': calorielimit,
               'Calorieconsumed': calorieconsumed, 'calorieleft': calorieleft}

    return render(request, 'profile.html', context)


class DeleteFoodView(LoginRequiredMixin, generic.DeleteView):
    model = Selectfooditem
    template_name = 'deleteselectedfood.html'
    success_url = reverse_lazy('profile')


# @login_required(login_url='login')
# def EditCalorielimitView(request):
#     if request.method == 'POST':
#         user = CustomUser.objects.get(id=request.user.id)
#         user.calorielimit = request.POST.get('calorielimit')
#         user.save()
#         return redirect('manage/profile')

#     return render(request, 'calorielimit_edit.html')

class EditCalorielimitView (LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'calorielimit_edit.html'
    fields = ['calorielimit']
    success_url = reverse_lazy('profile')


