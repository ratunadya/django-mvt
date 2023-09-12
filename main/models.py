from django.db import models

# Create your models here.
class Item(models.Model):
    category_choices = (
        ('pendidikan', 'Pendidikan'),
        ('medis dan kesehatan', 'Medis dan Kesehatan'),
        ('lingkungan', 'Lingkungan'),
        ('bencana alam', 'Bencana Alam'),
        ('anak-anak', 'Anak-anak'),
        ('kemanusiaan', 'Kemanusiaan'),
        ('zakat', 'Zakat'),
        ('wakaf', 'Wakaf'),
        ('panti asuhan', 'Panti Asuhan'),
        ('hewan', 'Hewan'),
    )
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    goal_amount = models.IntegerField()
    category = models.CharField(max_length=100, choices=category_choices, default='pendidikan')
    description = models.TextField()
