from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# name, location, address
class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE )


# user, branch, image, date_of_birth
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user} Profile'

        # creating our own save method/ overwriting the save method

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # make instance of image and pass the path to it
        img = Image.open(self.image.path)

        # resizing the image.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



