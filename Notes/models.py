from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    id_prev = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.title}"
    
class Item(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    note = models.ForeignKey(Note, related_name="mother_note", on_delete=models.CASCADE)
    id_next = models.ForeignKey(Note, related_name="child_note", on_delete=models.CASCADE)
    is_complete = models.BooleanField()
    
    def __str__(self) -> str:
        return f"{self.title}, {str(self.note)}"