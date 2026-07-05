from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    SERVICE_CHOICES = [
    ('Website Development', 'Website Development'),
    ('Landing Page', 'Landing Page'),
    ('Logo Design', 'Logo Design'),
    ('Photo Editing', 'Photo Editing'),
    ('Video Editing', 'Video Editing'),
]

    service = models.CharField(
    max_length=50,
    choices=SERVICE_CHOICES
)
    budget = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name