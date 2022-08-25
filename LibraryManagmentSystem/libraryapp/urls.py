from django.contrib import admin
from django.urls import path
from libraryapp import views
from LibraryManagmentSystem import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('save/',views.save,name='save'),
    path('login/',views.login,name='login'),
    path('validate/',views.validate,name='validate'),
    path('addbooks/',views.addbooks.as_view(),name='addbooks'),
    path('allbook/',views.allbook.as_view(),name='allbook'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)