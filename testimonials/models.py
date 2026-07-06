from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name