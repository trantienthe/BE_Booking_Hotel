from django.db import models

from .room import Room
from .utilities import  Utilities

class RoomUtilities(models.Model):
    id_room_utilities = models.AutoField(primary_key=True)
    utilities = models.ForeignKey(Utilities, on_delete=models.CASCADE, related_name='room_utilities')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_utilities')

    def __str__(self):
        return f"{self.room} - {self.utilities}"