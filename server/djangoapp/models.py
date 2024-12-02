from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Assuming CarMake model is already defined as per your previous requirements
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model
class CarModel(models.Model):
    # ForeignKey to CarMake model (Many-to-One relationship)
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name='car_models'
    )

    # Dealer ID (IntegerField), 
    # assuming it refers to a dealer in an external Cloudant database
    dealer_id = models.IntegerField()

    # Car model name (e.g., "Corolla", "X5")
    name = models.CharField(max_length=100)

    # Type of car (Sedan, SUV, Wagon, etc.)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more car types as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    # Year of manufacture
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ],
        default=2023,
    )

    # Optional description for the car model
    description = models.TextField(blank=True, null=True)

    # Optional price field
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    # String representation of the car model 
    # (returns both car make and model name)
    def __str__(self):
        return (
            f"{self.car_make.name} {self.name} ({self.type}, {self.year})"
        )
