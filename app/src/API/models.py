from django.db import models



# class MachineModelType(models.Model):
#     model_type = models.CharField(max_length=15,)


class CoffeMachine(models.Model):

    title                 = models.CharField(max_length=15, unique=True)
    model_type            = models.CharField(max_length=15)
    product_type          = models.CharField(max_length=70, )
    water_line_compatible = models.BooleanField()



# class PodType(models.Model):
#     model_type = models.CharField()

# I chose not to make seperate models for classes, It would be more robust
# but also more cumbersome. So I chose flexibility over robustness.
class CoffePod(models.Model):

    title         = models.CharField(max_length=15, unique=True)
    product_type  = models.CharField(max_length=70, )
    coffee_flavor = models.CharField(max_length=200,)
    pack_size     = models.IntegerField()