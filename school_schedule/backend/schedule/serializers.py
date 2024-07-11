from rest_framework import serializers
from .models import Class, Subject, Schedule

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class_name = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Schedule
        fields = '__all__'
