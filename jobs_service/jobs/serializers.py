import requests
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def validate_created_by_user(self, value):
        """Check if the user exists in users_service"""
        users_service_url = f"http://127.0.0.1:8000/api/user_details/{value}/"  # Make sure this is correct

        response = requests.get(users_service_url)

        if response.status_code != 200:
            raise serializers.ValidationError("User does not exist in users service")

        return value
