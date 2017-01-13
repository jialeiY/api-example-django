from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^update_message/$',views.update_message,name='msg'),
    url(r'^save_message/$',views.save_message,name='msg2')

]
