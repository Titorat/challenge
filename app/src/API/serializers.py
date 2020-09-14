from rest_framework import serializers 
from API.models import CoffeMachine,CoffePod
 
 
class CoffeMachineSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CoffeMachine
        fields = ('title',
                  'model_type',
                  'product_type',
                  'water_line_compatible')

class CoffePodSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CoffePod
        fields = ('title',
                  'product_type',
                  'coffee_flavor',
                  'pack_size')