from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# @login_required
# def dashboard(request):
#     user = request.user
#     if user.user_type == 'doctor':
#         return render(request, 'doctor_dashboard.html')
#     else:
#         return render(request, 'patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def dashboard(request):
    user = request.user
    if user.user_type == 'doctor':
        return redirect('doctor_dashboard')
    else:
        return redirect('patient_dashboard')