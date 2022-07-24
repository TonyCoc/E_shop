from django.contrib.auth import authenticate
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from django.test import TestCase,Client

#cant write Test because of staff required decorator in views