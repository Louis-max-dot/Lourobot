from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages,auth
from robotapp.models import Profile
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe


# Create your views here.
def home(request):
     return render(request, "index.html")

def register(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")
          confirm_pass = request.POST.get("confirm_password")
          is_valid = True

          if not(username and password  and confirm_pass):
               messages.error(request, "All fields are required")
               is_valid = False
          if (password!=confirm_pass):
               messages.error(request,"Passwords do not match")
               is_valid = False
          if User.objects.filter(username__iexact = username).exists():
               messages.error(request, "A user with the username already exists")
               is_valid = False
          if is_valid == False:
               return redirect ("user_creation")

          created_user = User.objects.create_user(username=username, password=confirm_pass,)
          messages.success(request,f"Hi,{created_user.username}")
          return redirect("login")
          
     return render(request,"users_m/create.html")


def login(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")
          

          user = auth.authenticate(username=username, password=password)

          if user is None:
               messages.error(request, "Invalid Credentials")
               return redirect("login")
          auth.login(request,user)
          return redirect("dashboard")

     return render(request,"users_m/login.html")




@login_required(login_url="login")
def dashboard(request):
     profile,_ = Profile.objects.get_or_create(user = request.user)
     if request.method == "POST":

          profile.email = request.POST.get("email")
          profile.message = request.POST.get("message")
          profile.save()

          valid = True

          if len(profile.message) <= 15:
               messages.error(request, "Please enter a detailed message")
               valid = False

          if "gmail.com" not in profile.email:
               messages.error(request,"Invaild email")
               valid = False

          if valid == False:
               return redirect(reverse("dashboard") + "#error" )

          

          send_mail(
               subject= "Alas a Profile message",
               message= f" from {profile.email}\n\n{profile.message}",
               fail_silently=False,
               from_email=None,
               recipient_list=[settings.DEFAULT_FROM_EMAIL]
  
          )

          send_mail(
               subject="Training Application",
               message="Thanks for applying to train with us\n We promise we won't dissapoint",
               fail_silently=False,
               from_email=None,
               recipient_list=[profile.email]
          )
          messages.success(request, "You have sucessfully been added to the training list")
          return redirect("users_list")

          

     
     context = {"profile": profile}    

     return render(request, "users_m/dashboard.html",context)

@login_required(login_url="login")
def users(request):
     users = User.objects.select_related("profile").all()
     context = {"all": users}
     return render(request,"users_m/users.html",context)

@login_required(login_url="login")
def edit_user(request,pk):
     user_to_edit = get_object_or_404(User,pk=pk)
     profile_to_edit = get_object_or_404(Profile, user=user_to_edit)
     current_user_id = request.user.id



     if current_user_id != user_to_edit.id:
          messages.error(request, mark_safe(f"You have been authenticated as <strong>{request.user.username}</strong> so you don't have to edit for another person except from you"))
          return redirect("users_list")
     
     if request.method == "POST":
          username = request.POST.get("username")
          email = request.POST.get("email")
          message = request.POST.get("message")

          if not (username and email and message):
               messages.error(request, "All fields are required")
               return redirect("edit_user", pk=pk)
          
          user_to_edit.username = username
          user_to_edit.save()
          profile_to_edit.email = email
          profile_to_edit.message = message
          profile_to_edit.save()


          messages.success(request, "You have edited your details suceesfilly")
          return redirect("users_list")
     

     context = {"user_to_edit": user_to_edit, "profile_to_edit": profile_to_edit}
     return render(request, "users_m/edit_user.html", context)

@login_required(login_url="login")
def delete_user(request, pk):
     user_to_delete = get_object_or_404(User,pk=pk)
     profile_to_del = get_object_or_404(Profile,user = user_to_delete)
     current_user = request.user

     if user_to_delete.id != current_user.id:
          messages.error(request, "Don't be wicked and delete another person from there")
          return redirect("users_list")

     if request.method == "POST":
          user_to_delete.delete()
          # messages.success(request, "You have deleted yourself successfully")
          return redirect("home")

    
     return render(request, "users_m/delete.html")

@login_required(login_url="login")
def logout(request):
     auth.logout(request)
     return redirect("home")


def contact(request):
     if request.method == "POST":
          
          firstName = request.POST.get("firstname")
          lastName = request.POST.get("lastname")
          message = request.POST.get("message").strip()
          email = request.POST.get("email").strip()
          valid = True

          if not (firstName and lastName and message and email):
               messages.error(request, "All fields are required")
               valid = False

          if "gmail.com" not in email:
               messages.error(request, "Email is Invalid")
               valid = False
          if len(message) <= 15:
               messages.error(request, "Please enter a short but understandable message")
               valid = False
          if valid == False:
               return redirect(reverse("home") + "#contacte" )


          send_mail(
               subject=f"{firstName} {lastName} contacted us",
               message=f"{message}; from {email}",
               from_email=None,
               recipient_list=[settings.DEFAULT_FROM_EMAIL],
               fail_silently=False     
          )
          messages.success(request, "Message Sent")
          return redirect(reverse("home") + "#contacte")


     return redirect("home") 





     











