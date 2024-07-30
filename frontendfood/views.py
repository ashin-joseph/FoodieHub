from django.shortcuts import render,redirect
from backendfood.models import fdCategoryDb,fbProductDb
from frontendfood.models import contactDb,signUpDb,cartDb, checkoutDb
import razorpay

def home_pg_fd(request):
    cdata=fdCategoryDb.objects.all()
    return render(request,"home_foodiee.html",{'cdata_f1':cdata})
def about_pg_fd(request):
    return render(request,"about_foodiee.html")
def booktable_pg_fd(request):
    return render(request,"booktable_foodiee.html")
def contact_pg_fd(request):
    return render(request,"contact_foodiee.html")
def contact_save_fd(request):
    if request.method=="POST":
        a=request.POST.get('c1')
        b=request.POST.get('c2')
        c=request.POST.get('c3')
        obj=contactDb(con_name=a,con_number=b,con_message=c)
        obj.save()
        return redirect(contact_pg_fd)
def menu_pg_fd(request):
    pdata=fbProductDb.objects.all()
    cdata=fdCategoryDb.objects.all()
    # Print cdata to the console
    # for item in cdata:
    #     print(f'Category Name: {item.c_name}, Category Class: {item.c_name}')
    return render(request,"menu_foodiee.html",{'pdata_f1':pdata,'cdata_f2':cdata})
def registration_pg_fd(request):
    return render(request,"registration_foodiee.html")
def save_registration_signup(request):
    if request.method=="POST":
        a=request.POST.get('e1')
        b=request.POST.get('e2')
        c=request.POST.get('e3')
        d=request.POST.get('e4')
        obj=signUpDb(su_email=a,su_username=b,su_password=c,su_confirmpassword=d)
        obj.save()
        return redirect(home_pg_fd)
def Login_su_fd(request):
    if request.method=="POST":
        su_un=request.POST.get('d1')
        su_pwd=request.POST.get('d2')
        if signUpDb.objects.filter(su_username=su_un,su_password=su_pwd).exists():
            request.session['su_username']=su_un
            request.session['su_password']=su_pwd
            return redirect(home_pg_fd)
        else:
            return redirect(registration_pg_fd)
    else:
        return redirect(registration_pg_fd)
def Logout_su_fd(request):
    del request.session['su_username']
    del request.session['su_password']
    return redirect(registration_pg_fd)
def detail_pg_fd(request,Proname):
    pdata=fbProductDb.objects.filter(p_name=Proname)
    return render(request,"details_foodiee.html",{'pdata':pdata})
def save_cart_foodiee(request):
    if request.method=="POST":
        a=request.POST.get("username")
        b=request.POST.get("productname")
        c=request.POST.get("quantity")
        d=request.POST.get("price")
        e=request.POST.get("totalprice")
        obj=cartDb(cart_username=a,cart_productname=b,cart_quantity=c,cart_price=d,cart_totalprice=e)
        obj.save()
        return redirect(menu_pg_fd)

def cart_pg(request):
    try:
        cartdata = cartDb.objects.filter(cart_username=request.session['su_username'])
        total_price = 0
        shipping_fee = 0
        total_shipping_Overall = 0

        for i in cartdata:
            total_price += i.cart_totalprice
            if total_price < 100:
                shipping_fee = 100
            else:
                shipping_fee = 0
            total_shipping_Overall = total_price + shipping_fee

        return render(request, "cart_foodiee.html", {
            'cartdata': cartdata,
            'total_price': total_price,
            'shipping_fee': shipping_fee,
            'total_shipping_Overall': total_shipping_Overall
        })

    except KeyError:
        # Handle the case when 'su_username' is not in session
        return render(request, "cart_foodiee.html", {
            'cartdata': [],
            'total_price': 0,
            'shipping_fee': 0,
            'total_shipping_Overall': 0
        })
def delete_cartItem(request,DCitem):
    cartDb.objects.get(id=DCitem).delete()
    return redirect(cart_pg)
def checkout_pg(request):
    cartdataUsername = cartDb.objects.filter(cart_username=request.session['su_username'])
    subTotal = 0
    shippingPrice = 0
    overAllTotal = 0
    for i in cartdataUsername:
        subTotal = subTotal + i.cart_price
        if subTotal < 100:
            shippingPrice = 100
        else:
            shippingPrice = 0
        overAllTotal = subTotal + shippingPrice
    return render(request, "checkout_foodiee.html",
                  {'cartdataUsername': cartdataUsername, 'subTotal': subTotal,
                   'shippingPrice': shippingPrice, 'overAllTotal': overAllTotal})
def save_checkout(request):
    if request.method=="POST":
        co_username= request.POST.get('name')
        co_email= request.POST.get('email')
        co_place= request.POST.get('place')
        co_address= request.POST.get('address')
        co_phone= request.POST.get('phone')
        co_message= request.POST.get('message')
        co_totalprice = request.POST.get('total')
        obj=checkoutDb(checkout_username=co_username,checkout_email=co_email,checkout_place=co_place,checkout_address=co_address,checkout_Phone=co_phone,checkout_message=co_message,checkout_overall_total=co_totalprice)
        obj.save()
        return redirect(payment_pg)
def payment_pg(request):
    customer=checkoutDb.objects.order_by('-id').first()
    pay =customer.checkout_overall_total
    amount = int(pay*100)
    pay_str = str(amount)
    for i in pay_str:
        print(i)
    if request.method =="POST":
        order_currency ='INR'
        client = razorpay.Client(auth=('rzp_test_7apnMZ22irzosy','mlTDHZRjKcZpIfDGoQVKW6WQ'))
        payment=client.order.create({'amount':amount, 'order_currency':order_currency,'payment_capture':'1'})

    return render(request,"payment_foodiee.html",{'customer':customer,'pay_str':pay_str})
