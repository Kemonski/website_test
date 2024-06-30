from django.db import models
from django.contrib.auth.models import User

class Games(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UsagiInfo(models.Model):
    user = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True)
    country = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)
class Profile(models.Model):
    user = models.OneToOneField(UsagiInfo, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=300, blank=True)
    games = models.ManyToManyField(Games, related_name='profile', blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True)
    Player_Type = {
        ('A', 'Competitive'),
        ('B', 'Casual'),
        ('C', 'Couch'),
        ('D', 'Discord Kitten'),
        ('E', 'Toxic'),
        ('F', 'Mommy')
    }
    status = models.CharField(max_length=1, choices=Player_Type)

    def __str__(self):
        return str(self.user)

class Client(models.Model):
    user = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True)
    country = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Info of {self.user}"

class Payment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    payment_method = models.CharField(max_length=50, null=True)
    start_session = models.TimeField(auto_now_add=True, null=True)
    end_session = models.TimeField(null=True)

    def __str__(self):
        return f"Session for {self.user} at {self.start_session} ends at {self.end_session}"

class Report(models.Model):
    Reporter = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reported_user')
    reported_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reported_user')
    reason = models.TextField(max_length=300, null=True)
    created_at_date = models.DateTimeField(auto_now_add=True)
    created_at_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.reported_user} report: (Date:{self.created_at_date}) (Time:{self.created_at_time})"