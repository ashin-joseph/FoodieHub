from django.shortcuts import render,redirect
from backendfood.models import fdCategoryDb,fbProductDb
from frontendfood.models import contactDb, booktableDb, reviewDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


def admin_pg_fd(request):
    return render(request,"admin_fd.html")
def admin_login_fd(request):
    if request.method=="POST":
        un=request.POST.get('l1')
        pwd=request.POST.get('l2')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"Welcome..")
                return redirect(index_pg)
            else:
                messages.warning(request,"Invalid user")
                return redirect(admin_pg_fd)
        else:
            messages.warning(request,"Undefine user")
            return redirect(admin_pg_fd)
def admin_logout_fd(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_pg_fd)
def index_pg(request):
    return render(request,"index.html")
def add_pg_c(request):
    return render(request,"add.html")
def save_add(request):
    if request.method=="POST":
        a=request.POST.get('a1')
        b=request.POST.get('a2')
        c=request.FILES['a3']
        obj=fdCategoryDb(c_name=a,c_description=b,c_picture=c)
        obj.save()
        messages.success(request,"Added Category")
        return redirect(add_pg_c)
def display_Pg_c(request):
    cdata=fdCategoryDb.objects.all()
    return render(request,"display_c.html",{'cdata':cdata})
def edit_pg_c(request,cEid):
    cdata=fdCategoryDb.objects.get(id=cEid)
    return render(request,"edit_c.html",{'cdata1':cdata})
def update_c(request,cUid):
    if request.method=="POST":
        a = request.POST.get('a1')
        b = request.POST.get('a2')
        try:
            c = request.FILES['a3']
            c_c=FileSystemStorage().save(c.name,c)
        except MultiValueDictKeyError:
            c_c=fdCategoryDb.objects.get(id=cUid).c_picture
        fdCategoryDb.objects.filter(id=cUid).update(c_name=a,c_description=b,c_picture=c_c)
        messages.warning(request,"Upadted category")
        return redirect(display_Pg_c)
def delete_c(request,cDid):
    fdCategoryDb.objects.filter(id=cDid).delete()
    messages.error(request,"Deleted category")
    return redirect(display_Pg_c)

def add_pg_p(request):
    cdata=fdCategoryDb.objects.all()
    return render(request,"add_p.html",{'cdata3':cdata})
def save_add_p(request):
    if request.method=="POST":
        a=request.POST.get('b1')
        b=request.POST.get('b2')
        c=request.POST.get('b3')
        d=request.POST.get('b4')
        e=request.POST.get('b5')
        f=request.FILES['b6']
        obj=fbProductDb(p_code=a,p_category=b,p_name=c,p_price=d,p_description=e,p_picture=f)
        obj.save()
        messages.success(request,"added product")
        return redirect(add_pg_p)
def display_pg_p(request):
    pdata=fbProductDb.objects.all()
    return render(request,"display_p.html",{'pdata':pdata})
def edit_pg_p(request,pEid):
    pdata=fbProductDb.objects.get(id=pEid)
    cdata=fdCategoryDb.objects.all()
    return render(request,"edit_p.html",{'pdata2':pdata,'cdata4':cdata})
def update_p(request,pUid):
    if request.method=="POST":
        a = request.POST.get('b1')
        b = request.POST.get('b2')
        c = request.POST.get('b3')
        d = request.POST.get('b4')
        e = request.POST.get('b5')
        try:
            f = request.FILES['b6']
            f_f=FileSystemStorage().save(f.name,f)
        except MultiValueDictKeyError:
            f_f=fbProductDb.objects.get(id=pUid).p_picture
        fbProductDb.objects.filter(id=pUid).update(p_code=a,p_category=b,p_name=c,p_price=d,p_description=e,p_picture=f_f)
        messages.info(request,"updated product")
        return redirect(display_pg_p)
def delete_p(request,pDid):
    fbProductDb.objects.filter(id=pDid).delete()
    messages.error(request,"deleted product")
    return redirect(display_pg_p)

def contact_fnfd_display(request):
    condata=contactDb.objects.all()
    return render(request,"fnfd_contac.html",{'condata':condata})
def delete_contact(request,conDid):
    contactDb.objects.filter(id=conDid).delete()
    messages.error(request,"Deleted Contact")
    return redirect(contact_fnfd_display)
def book_table_display(request):
    btdata= booktableDb.objects.all()
    return render(request, "display_bt.html",{'btdata':btdata})
def delete_booktable(request,Did):
    booktableDb.objects.filter(id=Did).delete()
    messages.error(request,"Deleted BookTable")
    return redirect(book_table_display)
def review_display(request):
    rdata=reviewDb.objects.all()
    return render(request, "display_review.html",{'rdata':rdata})
def delete_review(request,Did):
    reviewDb.objects.filter(id=Did).delete()
    messages.error(request,"Deleted Review")
    return redirect(review_display)