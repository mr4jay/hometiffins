from rest_framework import serializers
from .models import CustomerOrders


class CustomerOrdersSerializer(serializers.ModelSerializer):
    
      class Meta:
         model = CustomerOrders
      #    exclude = ['customer']
         fields = "__all__"
      #    read_only_fields =['customer']

         def save(self):
               customer = self.context['request.user']
         
      

# class LoginSerializer(serializers.Serializer):
#       email = serializers.CharField()
#       password = serializers.CharField()


# class ChangePasswordSerializer(serializers.Serializer):
#       old_password = serializers.CharField()
#       new_password = serializers.CharField()


# class ResetPasswordLinkSerializer(serializers.Serializer):
#       email= serializers.EmailField()


# class ResetPasswordsSerializer(serializers.Serializer):
#       password = serializers.CharField()
#       confirm_password = serializers.CharField()

     