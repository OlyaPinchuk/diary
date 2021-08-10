from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, UpdateAPIView, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response