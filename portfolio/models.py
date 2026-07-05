from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('Website', 'Website'),
        ('Logo', 'Logo'),
        ('Photo Editing', 'Photo Editing'),
        ('Video Editing', 'Video Editing'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    project_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title