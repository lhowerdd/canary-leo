from django.shortcuts import render


# Create your views here.

def create_community(request):
    return render(request, 'create_community.html')


# Admin home view - displays the home view for the admin of a community
def admin_community_home(request):
    return render(request, 'communityadmin/admin_community_home.html')


# def for saving a community after creation
def save_community(request):

    name = request.POST.get('name')
    password = request.POST.get('password')
    admin = request.user

    community = Community(community_name=name, password=password, admin=admin)

    # Save the report to the database
    community.save()
