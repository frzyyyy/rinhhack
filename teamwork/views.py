from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from teamwork.forms import LoginForm, RegisterForm


def settings(request):
    return render(request, 'teamwork/settings.html')


def notifications(request):
    return render(request, 'teamwork/notifications.html')


def colleagues(request):
    return render(request, 'teamwork/colleagues.html')


def meetings(request):
    return render(request, 'teamwork/meetings.html')


def tasks(request):
    return render(request, 'teamwork/tasks.html')


def home(request):
    return render(request, 'teamwork/home.html')


def account(request):
    if not request.user.is_authenticated:
        return redirect('authorization')
    return render(request, 'teamwork/account.html', {'user': request.user})


def doLogout(request):
    logout(request)
    return redirect('authorization')


def authorization(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('account')
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'teamwork/authorization.html', {'form': form})


def registration(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['icon'])
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('authorization')
    return render(request, 'teamwork/registration.html', {'form': form})


def handle_uploaded_file(f):
    with open(f"teamwork/uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    return render(request, 'teamwork/index.php')


def task(request):
    return render(request, 'teamwork/task.php')

