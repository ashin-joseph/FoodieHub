from django.urls import path
from frontendfood import views


urlpatterns = [
    path('',views.home_pg_fd,name="Homepage"),
    path('Aboutpage/',views.about_pg_fd,name="Aboutpage"),
    path('Book_tablepage/',views.booktable_pg_fd,name="Book_tablepage"),
    path('Contactpage/',views.contact_pg_fd,name="Contactpage"),
    path('Contactadd/',views.contact_save_fd,name="Contactadd"),
    path('Menupage/',views.menu_pg_fd,name="Menupage"),
    path('Registrationpage/',views.registration_pg_fd,name="Registrationpage"),
    path('SignUppage/',views.save_registration_signup,name="SignUppage"),
    path('LogInpage/',views.Login_su_fd,name="LogInpage"),
    path('LogOutpage/',views.Logout_su_fd,name="LogOutpage"),
    path('Detailpage/<Proname>/',views.detail_pg_fd,name="Detailpage"),
    path('SaveCart/',views.save_cart_foodiee,name="SaveCart"),
    path('Cartpage/',views.cart_pg,name="Cartpage"),
    path('checkOutpage/',views.checkout_pg,name="checkOutpage"),
    path('saveCheckout/',views.save_checkout,name="saveCheckout"),
    path('paymentpage/',views.payment_pg,name="paymentpage"),

    path('DeleteFromCart/<int:DCitem>/',views.delete_cartItem,name="DeleteFromCart"),
]