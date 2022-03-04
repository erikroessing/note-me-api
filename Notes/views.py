from rest_framework import viewsets
from Notes.models import Note, Item
from Notes.serializer import NotesSerializer, ItemsSerializer

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    
class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer