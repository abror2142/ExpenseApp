from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseAPIView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    

class OwnExpenseAPIView(APIView):
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            expenses = Expense.objects.filter(user=request.user.pk)
            serializer = ExpenseSerializer(expenses, many=True)
            return Response({"data": serializer.data})
        return Response({"messsage": "You have to be loggged in to view your expenses!"})
    