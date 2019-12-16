import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.db.models import Sum, Count, Max
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from catalog.choices import *
from PIL import Image, ExifTags
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userpic = models.FileField(upload_to='profilepictures', blank=True, null=True)
    homecity = models.CharField(max_length=30, blank=True, null=True)
    number_rating = models.IntegerField(blank=True, null=True)
    high_rating = models.CharField(max_length=45, blank=True, null=True)
    last_rating = models.CharField(max_length=45, blank=True, null=True)

    def get_user_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('userdetail', args=[str(self.user)])

    def __str__(self):
        return '%s' % self.user

@receiver(post_save, sender=Profile, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):

    def rotate_image(filepath):
        try:
            image = Image.open(filepath)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
            image.save(filepath)
            image.close()
        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass

    if instance.userpic:
      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      fullpath = BASE_DIR + '/catalog/static' + instance.userpic.url
      rotate_image(fullpath)

    # def rotate_image(self, *args, **kwargs):
    #     if self.userpic:
    #         pilImage = Img.open(BytesIO(self.userpic.read()))
    #         for orientation in ExifTags.TAGS.keys():
    #             if ExifTags.TAGS[orientation] == 'Orientation':
    #                 break
    #         exif = dict(pilImage._getexif().items())
    #
    #         if exif[orientation] == 3:
    #             pilImage = pilImage.rotate(180, expand=True)
    #         elif exif[orientation] == 6:
    #             pilImage = pilImage.rotate(270, expand=True)
    #         elif exif[orientation] == 8:
    #             pilImage = pilImage.rotate(90, expand=True)
    #
    #         output = BytesIO()
    #         pilImage.save(output, format='JPEG', quality=75)
    #         output.seek(0)
    #         self.userpic = File(output, self.userpic.name)
    #
    #     return super(Profile, self).rotate_image(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class MasterAddModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60) # blank=True, null=True
    rating = models.CharField(max_length=30, blank=True, null=True)
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name

#### FULL ADD MODEL #####

class CleanReviewModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60) # blank=True, null=True
    rating = models.CharField(max_length=30,blank=True, null=True)
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    ave_rating = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    count_rating = models.IntegerField(blank=True, null=True)

@receiver(post_save, sender=MasterAddModel)
def build_clean(sender, instance, **kwargs):

    count_rating = MasterAddModel.objects.filter(name=instance.name).exclude(rating="").count()

    sum_alltime = MasterAddModel.objects.filter(name=instance.name, rating="5").count() * 5
    sum_love = MasterAddModel.objects.filter(name=instance.name, rating="4").count() * 4
    sum_like = MasterAddModel.objects.filter(name=instance.name, rating="3").count() * 3
    sum_meh = MasterAddModel.objects.filter(name=instance.name, rating="2").count() * 2
    count_wish = MasterAddModel.objects.filter(name=instance.name, rating="").count()

    if (count_rating - count_wish) > 0:
        sum_ratings = sum_alltime + sum_love + sum_like + sum_meh
    else:
        sum_ratings = None

    try:
        ave_rating = sum_ratings / count_rating
    except:
        ave_rating = None


    CleanReviewModel.objects.update_or_create(
    name=instance.name,
    user=instance.user,
    defaults = {
    'rating': instance.rating,
    'perfect_for': instance.perfect_for,
    'notes': instance.notes,
    'city': instance.city,
    'country': instance.country,
    'address': instance.address,
    'category1': instance.category1,
    'category2': instance.category2,
    'category3': instance.category3,
    'postcode': instance.postcode,
    'suburb': instance.suburb,
    'date': instance.date,
    'temperature': instance.temperature,
    'ave_rating': ave_rating,
    'count_rating': count_rating,
    })

class SingleLocationRecord(models.Model):
    name = models.CharField(max_length=60) # blank=True, null=True
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    country = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    category1 = models.CharField(max_length=30,blank=True, null=True)
    category2 = models.CharField(max_length=30,blank=True, null=True)
    category3 = models.CharField(max_length=30,blank=True, null=True)
    postcode = models.CharField(max_length=30,blank=True, null=True)
    suburb = models.CharField(max_length=30,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    count_ratings = models.IntegerField(blank=True, null=True)
    count_wishlist = models.IntegerField(blank=True, null=True)
    ave_ratings = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

@receiver(post_save, sender=CleanReviewModel)
def build_single(sender, instance, **kwargs):

    # count_ratings = CleanReviewModel.objects.filter(name=instance.name, rating__isnull=False).count()
    count_wishlist = CleanReviewModel.objects.filter(name=instance.name, rating="").count()

    SingleLocationRecord.objects.update_or_create(
    name=instance.name,
    defaults = {
    'perfect_for': instance.perfect_for,
    'notes': instance.notes,
    'city': instance.city,
    'country': instance.country,
    'address': instance.address,
    'category1': instance.category1,
    'category2': instance.category2,
    'category3': instance.category3,
    'postcode': instance.postcode,
    'suburb': instance.suburb,
    'date': instance.date,
    'temperature': instance.temperature,
    'count_ratings': instance.count_rating,
    'count_wishlist': count_wishlist,
    'ave_ratings': instance.ave_rating,
    })














#

##### TEST PAGES #####
class TestEntryModel(models.Model):
    name = models.CharField(max_length=30, default="New", blank=True, null=True)

class TestStoreModel(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

@receiver(post_save, sender=TestEntryModel)
def single_save(sender, instance, **kwargs):
    TestStoreModel.objects.update_or_create(name=instance.name)











##### DRINK PAGES ######

class DrinkCreateNewModel(models.Model):
    day = models.CharField(max_length=30, blank=True, null=True) # blank=True, null=True
    drinks = models.IntegerField(blank=True, null=True)
    waters = models.IntegerField(blank=True, null=True)
    maxBAC = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)

class DrinkCreateNewModelDetails(models.Model):
    day = models.CharField(max_length=30, blank=True, null=True) # blank=True, null=True
    drinks = models.IntegerField(blank=True, null=True)
    waters = models.IntegerField(blank=True, null=True)
    maxBAC = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

class DrinkCreateNewModelFinal(models.Model):
    day = models.CharField(max_length=30, blank=True, null=True)
    drinks = models.IntegerField(blank=True, null=True)
    waters = models.IntegerField(blank=True, null=True)
    maxBAC = models.DecimalField(max_digits=3, decimal_places=2,blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    highBAC = models.CharField(max_length=30, blank=True, null=True)

@receiver(post_save, sender=DrinkCreateNewModel)
def drink_setup(sender, instance, **kwargs):
    DrinkCreateNewModelFinal.objects.update_or_create(
    day=instance.day, date=instance.date)

@receiver(post_save, sender=DrinkCreateNewModelDetails)
def drink_details(sender, instance, **kwargs):

    try:
        currentBAC = DrinkCreateNewModelFinal.objects.get(day=instance.day).maxBAC

        if instance.maxBAC > currentBAC:
            maxBAC = instance.maxBAC
        else:
            maxBAC = currentBAC
    except:
        maxBAC = 0


    try:
        create_date = DrinkCreateNewModel.objects.get(day=instance.day).date
    except:
        create_date = None

    if maxBAC > 0.05:
        highBAC = "Yes"
    else:
        highBAC = "No"

    DrinkCreateNewModelFinal.objects.update_or_create(
    day=instance.day,
    defaults={
    'drinks': instance.drinks,
    'waters': instance.waters,
    'maxBAC': maxBAC,
    'date': create_date,
    'highBAC': highBAC,
    })
