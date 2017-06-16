from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView
from rest_framework import generics
from rest_framework.exceptions import NotFound

from .serializers import TaskSerializer, TasklistSerializer
from .models import Task, Tasklist


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/todolists/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)

        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class TasklistCreateView(generics.ListCreateAPIView):
    serializer_class = TasklistSerializer

    def get_queryset(self):
        queryset = Tasklist.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TasklistSerializer

    def get_queryset(self):
        queryset = Tasklist.objects.filter(owner=self.request.user)
        return queryset


class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        list_id = self.kwargs.get('list_id', None)
        queryset = Task.objects.filter(tasklist__owner=self.request.user,tasklist_id = list_id)
        return queryset

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id', None)
        try:
            tasklist = Tasklist.objects.get(pk=list_id, owner=self.request.user)
        except Tasklist.DoesNotExist:
            raise NotFound()
        serializer.save(tasklist=tasklist)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def get_queryset(self):
        tasklist1 = Tasklist.objects.filter(owner=self.request.user)
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            tasklist1 = tasklist1.filter(id=list_id)
            if tasklist1.owner == self.request.user:
                queryset = Task.objects.filter(tasklist=tasklist1)
        return queryset