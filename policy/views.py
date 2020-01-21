from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PolicySerializer, PaymentSerializer
from .models import Policy
# Create your views here.


@api_view(['GET', 'POST'])
def create_policy(request):
	serializer = PolicySerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_payment(request):
	data = request.data
	serializer = PaymentSerializer(data=data)
	if serializer.is_valid():
		try:
			policy = Policy.objects.get(user_ext_id=data['user_ext_id'], benefits=data['benefits'], currency=data['currency'])
			if policy.total_max_amount >= data['amount']:
				policy.total_max_amount = policy.total_max_amount - data['amount']
				policy.save()
				serializer.save()
				return Response({"authorized": True, "reason": None}, serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response({"authorized": False, "reason": "POLICY_AMOUNT_EXCEEDED"}, status=status.HTTP_200_OK)
		except:
			policy = None
			return Response({"authorized": False, "reason": "POLICY_NOT_FOUND"}, serializer.data, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
