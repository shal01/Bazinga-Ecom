from rest_framework.serializers import ModelSerializer
from .models import ItemModel

class ItemSerializers(ModelSerializer):
    
    class Meta:
        model = ItemModel
        fields = '__all__'