from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^patient_list$',views.patient_list,name='patient_list'),
]
