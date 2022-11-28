from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import random
from django.db.models import Sum
from datetime import datetime
from home.models import Destination , Booking 
from django.contrib import messages





# <------------------Global Method Send Email Function Start here ------------------------------>
def send_email(sub,message,reciver_email):
    try:
        send_mail(
        ''+sub+'',
        ''+message+'',
        'inft.20101a0019@gmail.com',
        [reciver_email],
        fail_silently=False,
        )
        return 1
    except:
        return 0







# Create your views here.

def check_avalibility(request):
    def check_count(place_code,data):
        if (Booking.objects.filter(place_code=place_code).filter(date=date).exists()):
            total_count = Booking.objects.filter(place_code=place_code).filter(date=date).aggregate(Sum('count'))
            return(total_count["count__sum"])
        else:
            return 0
    if request.method =="POST":
        date = request.POST.get("date")
        slot = request.POST.get("slot")
        count = request.POST.get("count")
        place_code = request.POST.get("place_code")
        if Destination.objects.filter(place_code=place_code).exists():
            return HttpResponse(20-int(check_count(place_code,date)))
        return HttpResponse("-1")

def index(request):
    dests = Destination.objects.all().order_by('-id')[:4]
    #dests = Destination.objects.all()
    lst = [i for i in dests]
    context = {
        "lst":lst
    }
    return render(request, 'index.html', context=context)
    

def tourism(request):
    dests = Destination.objects.all()
    lst = [i for i in dests]
    context = {
        "lst":lst
    }
    return render(request,'tourism.html', context=context)


def information(request):
    place_code = request.GET.get("place_code")
    
    try:
        dests = Destination.objects.all().filter(place_code=place_code)
        lst = [i for i in dests]
        context = {
            "lst":lst
        }
        return render(request,'information.html', context=context)
    except:
        return HttpResponse("<h1 style='color:red;'>Something went Wrong.!!</h1>")
    
      

def booking(request):
    return render(request,'booking.html')

def booking2(request):
    def booking_id_generate():
        booking_id=random.randrange(1000000,10000000)
        if (Booking.objects.filter(booking_id=booking_id).exists()):
            booking_id_generate()
        else:
            return booking_id
    if request.user.is_authenticated:
        if request.method =="POST":
            name = request.POST.get("name")
            adhar = request.POST.get("adhar")
            age = request.POST.get("age")
            slot = request.POST.get("slot")
            gender = request.POST.get("gender")
            count = request.POST.get("count")
            place_code = request.POST.get("place_code")
            date = request.POST.get("date")
            destination_data =Destination.objects.filter(place_code=place_code).values('name')
            place_name=destination_data[0]["name"]
            booking_id=booking_id_generate()
            user = Booking.objects.create(booking_id=booking_id,slot=slot,date=date,booking_owner=request.user.username,
            persons_adhar=adhar,count=count,persons_name=name,place_code=place_code,persons_age=age,persons_gender=gender,place_name=place_name).save()
            sub = 'About Booking'
            message = f'Your Booking for {place_name} is done....On Date {date} for slot {slot} and no. of person {count}. Your booking ID is -->  {booking_id} '
            reciver_email = request.user.email
            send_email(sub,message,reciver_email)
            return HttpResponse("1")

        else:
            place_code = request.GET.get("place_code")
            count = request.GET.get("count")
            date = request.GET.get("date")
            slot = request.GET.get("slot")
            destination_data =Destination.objects.filter(place_code=place_code).values()
            place_name=destination_data[0]["name"]
            context = {
                "place_name":place_name,
                "sign_in":1,
                "count":count,
                "slot":slot,
                "date":date,
                "place_code":place_code,
            }
            return render(request,'booking2.html',context=context)
    return render(request,'booking2.html',context={"sign_in":0,'count':0,})
    

# def contactus(request):
#      if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         phonenumber = request.POST['phonenumber']
#         desc = request.POST['desc']
#         print(name,email,phonenumber,desc)
#         contactus = Contactus(name=name, email=email, phonenumber=phonenumber, desc=desc, date=datetime.today())
#         contactus.save()
#         messages.success(request, 'Your form has been submitted...')
#      return render(request,'contactus.html')

def MyBookings(request):
    if request.user.is_authenticated:
        booking_data=Booking.objects.all().filter(booking_owner=request.user.username).values()
        context={
            'booking_data':booking_data,
        }
        return render(request,'MyBookings.html',context=context)
    else:
        return render(request,'MyBookings.html',context={'sign_in':0})


def booking_info(request):
    booking_id = request.GET.get('booking_id')
    print(booking_id)
    if request.user.is_authenticated:
        booking_data=Booking.objects.all().filter(booking_id=booking_id).values()
        context={
            'booking_data':booking_data,
        }
        return render(request,'booking_info.html',context=context)
    else:
        return redirect('/')



    



# <------------------Autintication sign in sign up class start here------------------------------>
class Auth:

    #< **********Common function to check redundancy of username , email or phone in database********>
    def check_redundent_info(email,username,password):
            # Now Perform some validation If Username , Number or email exists in database
            if User.objects.filter(password=password).exists():
                #send 0 to show password exist in db
                return 1
            elif User.objects.filter(username=username).exists():
                #send 2 to show username exist in db
                return 0
            elif User.objects.filter(email=email).exists():
                #send 2 to show email exist in db
                return 2                               
            else:
                #ereturn 3 to say all ok
                return 3

    #< **********End of Common function to check redundancy of username , email or phone in database********>
         # <------------------Send otp is start here------------------------------>
    # def send_otp(request):
    #     if request.method =='POST':
    #         email = request.POST.get('email')
    #         name = request.POST.get('name')
    #         password = request.POST.get("password")
    #         username = request.POST.get("username")
    #         # call function to check Redundancy of email , phone, username
    #         flag =Auth.check_redundent_info(email,username,password)
    #         if flag==3:
    #             otp = random.randrange(1000,10000)
    #             #call send msg function
    #             flag = send_email("Your otp For Signup",f"Hii {name},greeting from Agrorent Your Otp For Verfication Is --> {str(otp)}",email)
    #             if flag: #send otp if all work fine
    #                 return HttpResponse(otp)
    #             else:   #send -1 as error flag
    #                 return HttpResponse("-1")
    #         else:
    #             return HttpResponse(str(flag))

      # <---------------------------Signin  Function is start here------------------------------>

    def sign_in(request):
        if request.method =="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate( request,username=username, password=password)
            # check if user entered correct crediantials
            if user is not None:
                login(request, user)
                #send Signal 1 to indicate login succesfully
                return HttpResponse("1")
                # return redirect("/")
                # A backend authenticated the credentials
            else:
                # No backend authenticated the credentials
                #send Signal 0 to indicate Something went Wrong
                return HttpResponse("0")
        else:
          return render(request,"index.html")


    

        # <------------------Signup function is start here------------------------------>

    def sign_up(request):
        # cHECK FOR pOST method and get the All required field
        if request.method =='POST':
            password = request.POST.get("password")
            username = request.POST.get("username")
            email=request.POST.get("email")
            name=request.POST.get("name")
            # call function to check Redundancy of email , phone, username
            flag = Auth.check_redundent_info(email,username,password)
            if flag==3:
                user = User.objects.create_user(username=username, password=password, email=email,first_name=name).save()
                #send 3 to Indicate All Above Mentioned Field Are Unique And saved succesully.
                return HttpResponse(3)
            else:
                return HttpResponse(str(flag))

        return render(request,"index.html")

    # <------------------Logout/Sign-out  function is start here------------------------------>

    def sign_out(request):
        logout(request)
        return redirect("/")
        




   

    