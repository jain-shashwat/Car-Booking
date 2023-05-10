from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import BookingForm
from .models import Event,Booking
# Create your views here.
# def home(request):
#     events=Event.objects.all()
#     return  HttpResponse('nameste admin')

class Home(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all()

# class Detail(generic.DetailView):
#     model = Event
#     template_name = 'home/detail.html'

def detail(request,pk):
    object=Event.objects.get(pk=pk)
    form=BookingForm

    return render(request,'home/detail.html',{'object':object,'form':form})


def check_avai(request,id):
    object = Event.objects.get(id=id)
    total_paltinum_seats = object.platinum_seats
    total_gold_seats = object.gold_seats
    total_silver_seats = object.silver_seats
    last_date=object.last_date


    check_total_platinum_seats=0
    check_total_gold_seats=0
    check_total_silver_seats=0
    
    time_preference=request.POST.get('time_preference')
    booking_date=request.POST.get('booking_date')
    event_name=request.POST.get('event_name')
    for_same_date=Booking.objects.filter(booking_date=booking_date)
    for_same_event_name=for_same_date.filter(event_name=event_name)
    for_same_time_preference=for_same_event_name.filter(time_preference=time_preference)

    for i in for_same_time_preference:
        check_total_platinum_seats += i.platinum_seats
        check_total_gold_seats += i.gold_seats
        check_total_silver_seats += i.silver_seats

    message=''
    if check_total_platinum_seats < total_paltinum_seats:
        rest_platinum_seats = total_paltinum_seats - check_total_platinum_seats
        message += f'paltinum_seats:{rest_platinum_seats},'
    else:
        message += 'No Platinum Seats Avaiable for your given Requirement '

    if check_total_gold_seats < total_gold_seats:
        rest_gold_seats = total_gold_seats - check_total_gold_seats
        message += f'Gold seats:{rest_gold_seats},'
    else:
        message += 'No Gold Seats Avaiable for your given Requirement'

    if check_total_silver_seats < total_silver_seats:
        rest_silver_seats = total_silver_seats - check_total_silver_seats
        message += f'Silver seats:{rest_silver_seats},'
    else:
        message += 'No Silver Seats Avaiable for your given Requirement'

    if str(booking_date)>str(last_date):
        message='This Show is not Avaiable for your given date'

    messages.info(request, message)
    return render(request,'home/detail.html',{'object':object,'time_preference':time_preference,'booking_date':booking_date})
   

def booking(request,id):
    id=id
    form = BookingForm
    # TAKING TOTAL NUMBER OF SEATS FROM EVENT MODEL
    seats = Event.objects.get(id=id)
    total_paltinum_seats = seats.platinum_seats
    total_gold_seats = seats.gold_seats
    total_silver_seats= seats.silver_seats
    name=seats.name
    
    if request.method=='POST':
        id=id
        form=BookingForm(request.POST)
        if form.is_valid():         
            visitor_name=form.cleaned_data['visitor_name']
            phone_number=form.cleaned_data['phone_number']
            time_preference = form.cleaned_data['time_preference']
            paltinum_seats = form.cleaned_data['platinum_seats']
            gold_seats = form.cleaned_data['gold_seats']
            silver_seats = form.cleaned_data['silver_seats']
            booking_date = form.cleaned_data['booking_date']
            event_name=form.cleaned_data['event_name']

            print(paltinum_seats)

            get_price=Event.objects.filter(id=id)
            for i in get_price:
                platinum_price = i.platinum_price
                gold_price = i.gold_price
                silver_price = i.silver_price
                

            message=''
            check_total_platinum_seats=0
            check_total_gold_seats=0
            check_total_silver_seats=0

           

            for_same_date=Booking.objects.filter(booking_date=booking_date)
            for_same_event_name=for_same_date.filter(event_name=event_name)
            for_same_time_preference=for_same_event_name.filter(time_preference=time_preference)

            


            for i in for_same_time_preference:
                check_total_platinum_seats+=i.platinum_seats
                check_total_gold_seats+=i.gold_seats
                check_total_silver_seats+=i.silver_seats



            if check_total_platinum_seats<total_paltinum_seats:
                rest_platinum_seats=total_paltinum_seats-check_total_platinum_seats
                message+=f'paltinum_seats:{rest_platinum_seats},'
            else:
                message+='No Platinum Seats Avaiable for your given Requirement '

            if check_total_gold_seats<total_gold_seats:
                rest_gold_seats=total_gold_seats-check_total_gold_seats
                message+=f'Gold seats:{rest_gold_seats},'
            else:
                message+='No Gold Seats Avaiable for your given Requirement'

            if check_total_silver_seats<total_silver_seats:
                rest_silver_seats=total_silver_seats-check_total_silver_seats
                message+=f'Silver seats:{rest_silver_seats},'
            else:
                message+='No Silver Seats Avaiable for your given Requirement'


            
            check_total_platinum_seats+=paltinum_seats
            check_total_gold_seats+=gold_seats
            check_total_silver_seats+=silver_seats

            message+=f'Please  try to change the time slot for the same day booking and  for same seat type '




            if check_total_platinum_seats<total_paltinum_seats and check_total_gold_seats<total_gold_seats and check_total_silver_seats<total_silver_seats:
                message='your booking is done !thanks for using us visit again!'
                data=form.save()
                platinum_seats=data.platinum_seats
                gold_seats=data.gold_seats
                silver_seats=data.silver_seats
                visitor_name=data.visitor_name
                phone_number=data.phone_number
                total_platinum_price=platinum_seats*platinum_price
                total_gold_price=gold_seats*gold_price
                total_silver_price=silver_seats*silver_price
                booked_date=data.booking_date

                net_price=total_platinum_price+total_gold_price+total_silver_price

                messages.info(request, message)
                return HttpResponseRedirect(reverse('home:checkout',args=(visitor_name,phone_number,platinum_seats,gold_seats,silver_seats, total_platinum_price, total_gold_price,total_silver_price,net_price,booked_date)))

            messages.info(request,message)
            return HttpResponseRedirect(reverse('home:booking',args=(id,)))

        else:
            return HttpResponse('somthing went wrong',form.errors)

    return render(request,'home/booking.html',{'form':form,'id':id,'name':name})

def checkout(request,visitor_name,phone_number,platinum_seats,gold_seats,silver_seats, total_platinum_price, total_gold_price,total_silver_price,net_price,booked_date):
    return  render(request,'home/checkout.html',{'visitor_name':visitor_name,
             'phone_number':phone_number,
             'platinum_seats':platinum_seats,
             'gold_seats':gold_seats,
             'silver_seats':silver_seats,
             'total_platinum_price':total_platinum_price,
             'total_gold_price':total_gold_price,
             'total_silver_price':total_silver_price,
             'net_price':net_price,
             'booked_date':booked_date
             })


def search(request):
    searched=request.GET.get('q')
    # return HttpResponse('hello i am searched',searched)
    name=Event.objects.filter(name__contains=searched)
    city=Event.objects.filter(city__contains=searched)
    return render(request, 'home/search.html', {'name': name,'city':city})

