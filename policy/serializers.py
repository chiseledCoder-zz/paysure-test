from rest_framework import serializers
from .models import Policy, Payment, BENEFITS


class PolicySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ext_id = serializers.CharField(max_length=20)
    benefits = serializers.ChoiceField(choices=BENEFITS, default="dentist")
    currency = serializers.CharField(max_length=3)
    total_max_amount = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        return Policy.objects.create(**validated_data)


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_ext_id = serializers.CharField(max_length=20)
    benefits = serializers.ChoiceField(choices=BENEFITS, default="dentist")
    currency = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    timestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)
