from django.db       import models
from Users.models    import *
from Products.models import *
from django.core.validators import RegexValidator

# Create your models here.
class CustomerOrders(models.Model):
    int_validator     = RegexValidator(regex=r'^[0-9]')
    customer          = models.ForeignKey(User, on_delete=models.CASCADE, default= None)
    order             = models.ForeignKey(FoodProducts, on_delete=models.CASCADE)
    ordered_date_time = models.DateTimeField(auto_now_add=True)
    ordered_quantity  = models.CharField(max_length = 3, null= True, blank= True,validators=[int_validator])
    order_price       = models.CharField(max_length = 3, null=True,blank=True, validators=[int_validator])
    discount          = models.CharField(max_length = 3, null=True,blank=True,validators=[int_validator])
    final_price       = models.CharField(max_length = 3, null=True,blank=True,validators=[int_validator])
    is_delivered      = models.BooleanField(default = False)
    is_canceled       = models.BooleanField(default = False)
    reason_for_cancel = models.TextField(null=True, blank=True)

# user foreign key
# Orders
# no:of Orders
# price
# discount
# Email
# is_delivered
# is_canceled
# is_ticket rasised




