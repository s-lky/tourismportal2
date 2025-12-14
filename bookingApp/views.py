from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from attractionsApp.models import Attraction
from .forms import BookingForm

# Create your views here.
@login_required
def create_booking(request, attraction_id):
    """创建预订"""
    attraction = get_object_or_404(Attraction, id=attraction_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.attraction = attraction
            booking.save()
            messages.success(request, f'预订成功！总价：￥{booking.total_price}')
            return redirect('bookingApp:my_bookings')
    else:
        form = BookingForm()
    
    return render(request, 'booking/create.html', {
        'form': form,
        'attraction': attraction
    })

@login_required
def my_bookings(request):
    """我的订单列表"""
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'booking/list.html', {'bookings': bookings})

@login_required
def booking_detail(request, booking_id):
    """订单详情"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking/detail.html', {'booking': booking})