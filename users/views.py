from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

# === Register a New User ===
def register_view(request):
    if request.method == 'POST':
        # Bind form to POST data
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save user and log them in
            user = form.save()
            login(request, user)

            # Redirect to dashboard after successful registration
            return redirect('dashboard:dashboard_view')
    else:
        # Display blank registration form
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


# === Login View ===
def login_view(request):
    if request.method == 'POST':
        # Get username and password from form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If valid, log the user in
            login(request, user)

            # Redirect to the original destination if exists, otherwise to dashboard
            next_url = request.GET.get('next') or 'dashboard:dashboard_view'
            return redirect(next_url)
        else:
            # Show error if credentials are invalid
            messages.error(request, 'Invalid credentials')

    return render(request, 'users/login.html')


# === Logout View ===
def logout_view(request):
    # Logs out the current user
    logout(request)
    # Redirect to homepage/landing page
    return redirect('landing')
