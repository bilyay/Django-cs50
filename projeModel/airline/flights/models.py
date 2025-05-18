from django.db import models

# Create your models here.
class Airport(models.Model):
    
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Flight(models.Model):
    # One-to-many relationship with Airport
    # Cascade delete: if an airport is deleted, all flights associated with it are also deleted
    origin = models.ForeignKey(Airport, related_name="departures", on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name="arrivals", on_delete=models.CASCADE)

    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} - ({self.duration} minutes)"
    
class Passenger(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"  