from django.shortcuts import render

# Create your views here.
from   django.shortcuts        import   render
from   rest_framework.views    import   APIView
from   rest_framework          import   status
from   .models                 import   *
from   rest_framework          import   generics
from   .serializers            import   *
from   rest_framework.response import   Response
from   django.core.mail        import   send_mail
from   datetime                import   datetime


class CreateOrders(generics.CreateAPIView):
    
    serializer_class = CustomerOrdersSerializer
    def post(self, request, format=None):
        serializer = CustomerOrdersSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.validated_data['customer']
            
            print(customer.name)
            serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
            
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)

class UpdateOrders(APIView):
    serializer_class =CustomerOrdersSerializer

    def get(self,request,pk):
        queryset = CustomerOrders.objects.all().filter(pk = pk).values()
        return Response(queryset)

    def patch(self, request,pk):
        update_object = CustomerOrders.objects.get(pk= pk)
        serializer = CustomerOrdersSerializer(update_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response( data=serializer.data)
        return Response( data="wrong parameters")
