from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Tag
from .models import Tasklist


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tasklist.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True,
                                        slug_field="name",
                                        queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed', 'date_created',
                  'date_modified', 'due_date', 'priority', 'tasklist', 'tags')
        read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tasklist
        fields = ('name', 'tasks')
