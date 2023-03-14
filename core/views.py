from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import *
from django.core.paginator import *



def index(request):
	return render(request, 'index.html')



# ---------------------------------------------- AUth Views Start ------------------------------------------------------ #

@login_required
def home(request):
    cards = FlashCard.objects.all()
    context = {
        'cards' : cards,
        'title' : "Homepage",
    }
    return render(request, 'home.html', context)

def det(request):
	return render(request, 'det.html')

@login_required
def profile(request):

    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
            phone_number = request.POST['phone']
            how_did_you_hear_about_us = request.POST['how']
            what_will_you_use_paradox_for = request.POST['what']

            
            user_profile.phone_number = phone_number
            user_profile.how_did_you_hear_about_us = how_did_you_hear_about_us
            user_profile.what_will_you_use_paradox_for = what_will_you_use_paradox_for
            user_profile.save()
            return redirect("home")
    context = {
        'title' : 'Edit Profile',
        'user_profile' : user_profile,
    }

    return render(request, 'profile.html', context)

def login(request):
    user = request.user

    if user.is_authenticated:
        return redirect(home)

    context = {
        'title' : 'Login',
    }
    if request.method == 'POST':
        username = request.POST['username'] #Requesting Username
        password = request.POST['password'] #Requesting Password
    
        user = auth.authenticate(username=username, password=password)

        if user is not None: #Cheking If User Exists in the database
            auth.login(request, user) # Logs in User
            return redirect('home') # Redirects to home view
        else:
            messages.info(request, 'Invalid Username or Password') #Conditional Checking if credentials are correct
            return redirect('login')#Redirects to login if invalid

    else:
        return render(request, 'login.html', context)

def register(request):
    user = request.user

    if user.is_authenticated:
        return redirect(home)
    context = {
        'title' : 'Sign Up',
    }
    if request.method == 'POST':
        #Requesting POST data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #End of POST data request

        #Condition is executed if both passwords are the same
        if password == password2:
            if User.objects.filter(email=email).exists(): #Checking databse for existing data
                messages.info(request, "This email is already in use")#Returns Error Message
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            #Else condition executed if the above conditions are not fulfilled    
            else:
                ctx = {
                    'user' : username
                }
                message = get_template('mail.html').render(ctx)
                msg = EmailMessage(
                    'Welcome to Paradoxx',
                    message,
                    'Paradoxx',
                    [email],
                )
                msg.content_subtype ="html"# Main content is now text/html
                msg.send()
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)#Logs in USER



            #Create user model and redirect to edit-profile
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(owner=user_model, user_id=user_model.id)
            new_profile.save()
            return redirect('edit-profile')#Rediects to specified page once condition is met
        else:
            messages.info(request, "Passwords do not match")
            return redirect(register)

    else:
        return render(request, 'register.html', context)
    
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def science(request):
	flashcard = FlashCard.objects.filter(category="Science")
	context = {
		'flashcard' : flashcard,
		'title' : 'Science'
	}
    #Paginator Logic Start
	page = request.GET.get('page', 1)

	paginator = Paginator(flashcard, 2)

	try:
	    flashcards = paginator.page(page)
    
	except PageNotAnInteger

	except EmptyPage:
	    flashcards = paginator.page(paginator.num_pages)
	     
	return render(request, 'category.html', context)

@login_required
def art(request):
	flashcard = FlashCard.objects.filter(category="Art")
	context = {
		'flashcard' : flashcard,
		'title' : 'Art'
	}
	return render(request, 'category.html', context, {'title' : 'Flashcards on Art'})

@login_required
def history(request):
	flashcard = FlashCard.objects.filter(category="History")
	context = {
		'flashcard' : flashcard,
		'title' : 'History'
	}
	return render(request, 'category.html', context, {'title' : 'Flashcards on History'})

@login_required
def technology(request):
	flashcard = FlashCard.objects.filter(category="Technology")
	context = {
		'flashcard' : flashcard,
		'title' : 'Technology'
	}
	return render(request, 'category.html', context, {'title' : 'Technology'})

@login_required
def business(request):
	flashcard = FlashCard.objects.filter(category="Business")
	context = {
		'flashcard' : flashcard,
		'title' : 'Business'
	}
	return render(request, 'category.html', context, {'title' : 'Business'})

@login_required
def detail(request, slug):
	flashcard = FlashCard.objects.get(slug=slug)

	context = {
		'flashcard' : flashcard,
		'title' : flashcard
	}

	return render(request, 'det.html', context)

# ----------------------------------- Auth Views End ------------------------------ #

# Create your views here.
