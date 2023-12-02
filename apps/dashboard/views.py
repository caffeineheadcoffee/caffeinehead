from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.user.auth import admin_only


@login_required
@admin_only
def admin_home(request):
    return render(request, 'admins/adminhome.html')
