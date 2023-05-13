from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreateForm
from .models import User
from django.contrib import messages

def index(request):
    context = {
        'user_data': User.objects.all(),
    }
    return render(request, 'app/index.html', context)

def add(request):
    form = UserCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('user:index')

    context = {
        'user_data': form,
    }
    return render(request, 'app/user_add.html', context)

def update(request, pk):
    user = get_object_or_404(User, pk=pk)

    form = UserCreateForm(request.POST or None, instance=user)

    print("**********************")
    print(type(get_object_or_404))
    print(type(UserCreateForm))
    print("**********************")
    print(type(user))
    print(type(form))
    print("**********************")
    print(user)
    print(form)
    print("**********************")

    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'ユーザ情報を更新しました！！')
                return redirect('user:index')
            except:
                messages.error(request, 'ユーザ情報の更新に失敗しました！！')
    
    context = {
        'user_data': form,
        }
    
    print(context['user_data'])
    return render(request, 'app/user_update.html', context)

def delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    user.delete()
    return redirect('user:index')

