# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from social.apps.django_app.default.models import UserSocialAuth
import requests
from django.template import loader
from django.shortcuts import render
