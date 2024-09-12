from django.urls import path
from backendfood import views

urlpatterns = [
    path('Adminpage_Fd/',views.admin_pg_fd,name="Adminpage_Fd"),
    path('AdminLogin/',views.admin_login_fd,name="AdminLogin"),
    path('AdminLogout/',views.admin_logout_fd,name="AdminLogout"),


    path('Indexpage/',views.index_pg,name="Indexpage"),
    path('AddpageC/',views.add_pg_c,name="AddpageC"),
    path('saveadd/',views.save_add,name="saveadd"),
    path('DisplaypageC/',views.display_Pg_c,name="DisplaypageC"),
    path('EditpageC/<int:cEid>/',views.edit_pg_c,name="EditpageC"),
    path('UpdatepageC/<int:cUid>/',views.update_c,name="UpdatepageC"),
    path('DeletepageC/<int:cDid>/',views.delete_c,name="DeletepageC"),


    path('AddpageP/',views.add_pg_p,name="AddpageP"),
    path('saveaddP/',views.save_add_p,name="saveaddP"),
    path('DisplaypageP/',views.display_pg_p,name="DisplaypageP"),
    path('EditpageP/<int:pEid>/',views.edit_pg_p,name="EditpageP"),
    path('UpdatepageP/<int:pUid>/',views.update_p,name="UpdatepageP"),
    path('DeletepageP/<int:pDid>/',views.delete_p,name="DeletepageP"),


    path('ContactDisplay/',views.contact_fnfd_display,name="ContactDisplay"),
    path('Delete_contact/<int:conDid>/',views.delete_contact,name="Delete_contact"),

    path('BookTableDisplay/', views.book_table_display, name="BookTableDisplay"),
    path('Delete_booktable/<int:Did>/', views.delete_booktable, name="Delete_booktable"),

    path('ReviewDisplay/', views.review_display, name="ReviewDisplay"),
    path('Delete_review/<int:Did>/', views.delete_booktable, name="Delete_review"),

]