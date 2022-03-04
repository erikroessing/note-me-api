from rest_framework.serializers import ModelSerializer
from Notes.models import Note, Item

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'