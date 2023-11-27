from rest_framework import serializers
from .models import Subject,Staff,Student

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'