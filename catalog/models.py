from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.db.models import Sum, Count, Max
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from catalog.choices import *

# Create your models here.

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userpic = models.FileField(upload_to='profilepictures', blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    number_rating = models.IntegerField(blank=True, null=True)
    high_rating = models.CharField(max_length=45, blank=True, null=True)
    last_rating = models.CharField(max_length=45, blank=True, null=True)

    def get_user_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('userdetail', args=[str(self.user)])

    def __str__(self):
        return '%s' % self.user

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

    def __str__(self):
        return '%s' % self.name

#### FULL ADD MODEL #####

# class CleanReviewModel(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60) # blank=True, null=True
#     rating = models.CharField(max_length=30,blank=True, null=True)
#     perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     city = models.CharField(max_length=30,blank=True, null=True)
#     country = models.CharField(max_length=30,blank=True, null=True)
#     address = models.CharField(max_length=50,blank=True, null=True)
#     category1 = models.CharField(max_length=30,blank=True, null=True)
#     category2 = models.CharField(max_length=30,blank=True, null=True)
#     category3 = models.CharField(max_length=30,blank=True, null=True)
#     postcode = models.CharField(max_length=30,blank=True, null=True)
#     suburb = models.CharField(max_length=30,blank=True, null=True)
#     date = models.DateTimeField(auto_now=True, null=True)
#     temperature = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
#     ave_ratings = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
#
# @receiver(post_save, sender=MasterAddModel)
# def build_clean(sender, instance, **kwargs):
#
#     count_ratings = MasterAddModel.objects.filter(name=instance.name, rating__isnull=False).count()
#
#     sum_alltime = MasterAddModel.objects.filter(name=instance.name, rating="5").count() * 5
#     sum_love = MasterAddModel.objects.filter(name=instance.name, rating="4").count() * 4
#     sum_like = MasterAddModel.objects.filter(name=instance.name, rating="4").count() * 3
#     sum_meh = MasterAddModel.objects.filter(name=instance.name, rating="2").count() * 4
#     count_wish = MasterAddModel.objects.filter(name=instance.name, rating="").count()
#
#     if (count_ratings - count_wish) > 0:
#         sum_ratings = sum_alltime + sum_love + sum_like + sum_meh
#     else:
#         sum_ratings = None
#
#     try:
#         ave_ratings = sum_ratings / count_ratings
#     except:
#         ave_ratings = None
#
#
#     CleanReviewModel.objects.update_or_create(
#     name=instance.name,
#     user=instance.user,
#     defaults = {
#     'rating': instance.rating,
#     'perfect_for': instance.perfect_for,
#     'notes': instance.notes,
#     'city': instance.city,
#     'country': instance.country,
#     'address': instance.address,
#     'category1': instance.category1,
#     'category2': instance.category2,
#     'category3': instance.category3,
#     'postcode': instance.postcode,
#     'suburb': instance.suburb,
#     'date': instance.date,
#     'temperature': instance.temperature,
#     'ave_ratings': ave_ratings,
#     })
#
# class SingleLocationRecord(models.Model):
#     name = models.CharField(max_length=60) # blank=True, null=True
#     perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     city = models.CharField(max_length=30,blank=True, null=True)
#     country = models.CharField(max_length=30,blank=True, null=True)
#     address = models.CharField(max_length=50,blank=True, null=True)
#     category1 = models.CharField(max_length=30,blank=True, null=True)
#     category2 = models.CharField(max_length=30,blank=True, null=True)
#     category3 = models.CharField(max_length=30,blank=True, null=True)
#     postcode = models.CharField(max_length=30,blank=True, null=True)
#     suburb = models.CharField(max_length=30,blank=True, null=True)
#     date = models.DateTimeField(auto_now=True, null=True)
#     temperature = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
#     count_ratings = models.IntegerField(blank=True, null=True)
#     ave_ratings = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
#
# @receiver(post_save, sender=CleanReviewModel)
# def build_single(sender, instance, **kwargs):
#
#     count_ratings = CleanReviewModel.objects.filter(name=instance.name, rating__isnull=False).count()
#
#     SingleLocationRecord.objects.update_or_create(
#     name=instance.name,
#     defaults = {
#     'perfect_for': instance.perfect_for,
#     'notes': instance.notes,
#     'city': instance.city,
#     'country': instance.country,
#     'address': instance.address,
#     'category1': instance.category1,
#     'category2': instance.category2,
#     'category3': instance.category3,
#     'postcode': instance.postcode,
#     'suburb': instance.suburb,
#     'date': instance.date,
#     'temperature': instance.temperature,
#     'count_ratings': count_ratings,
#     'ave_ratings': instance.ave_ratings,
#     })

#### FULL ADD MODEL #####







#### OLD VERSION MODELS ######
class AddReview(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="New") # blank=True, null=True
    location = models.CharField(choices=LOCATION, max_length=30, blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30, blank=True, null=True)
    spotpic = models.FileField(upload_to='spotpictures', blank=True, null=True)
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10), MinValueValidator(0)], blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.name

class SingleLocation(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(choices=LOCATION, max_length=30, blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30, blank=True, null=True)
    countrating = models.IntegerField(blank=True, null=True)
    averating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10), MinValueValidator(0)], blank=True, null=True)
    load_image = models.FileField(upload_to='spotpictures', blank=True, null=True)
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('userspotdetail', args=[str(self.name)])

    def __str__(self):
        return '%s' % self.name

@receiver(post_save, sender=AddReview)
def single_spot_save(sender, instance, **kwargs):
    count_rating = AddReview.objects.filter(name=instance.name, rating__isnull=False).count()
    sum_rating = list(AddReview.objects.filter(name=instance.name).aggregate(Sum('rating')).values())[0]

    if count_rating == 0:
        ave_rating = 0
    else:
        ave_rating = sum_rating / count_rating

    img_test = instance.spotpic
    if img_test is None:
        load_image is None
    else:
        load_image = instance.spotpic



    SingleLocation.objects.update_or_create(
    name=instance.name,
    defaults = {
    'location': instance.location,
    'category': instance.category,
    'countrating': count_rating,
    'averating': ave_rating,
    'load_image': load_image,
    })

class ReviewRecord(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="New") # blank=True, null=True
    location = models.CharField(choices=LOCATION, max_length=30, blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=30, blank=True, null=True)
    spotpic = models.FileField(upload_to='spotpictures', blank=True, null=True)
    perfect_for = MultiSelectField(choices=PERFECT_FOR, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10), MinValueValidator(0)], blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)

@receiver(post_save, sender=AddReview)
def clean_register(sender, instance, **kwargs):
    ReviewRecord.objects.update_or_create(
    user=instance.user,
    name=instance.name,
    defaults = {
    'location': instance.location,
    'category': instance.category,
    'spotpic': instance.spotpic,
    'perfect_for': instance.perfect_for,
    'notes': instance.notes,
    'rating': instance.rating,
    'date': instance.date,
    })

@receiver(pre_save, sender=AddReview)
def add_favorite(sender, instance, **kwargs):

    high_rating = list(AddReview.objects.aggregate(Max('rating')).values())[0]
    try:
        high_rating_name = AddReview.objects.get(rating=high_rating).name
    except:
        high_rating_name = "No spots added"

    try:
        if instance.rating > high_rating:
            Profile.objects.update_or_create(
            user=instance.user,
            defaults = {
            'high_rating': instance.name
            })
        else:
            pass
    except:
        pass

@receiver(post_save, sender=AddReview)
def add_user_overview(sender, instance, **kwargs):
    count_rating = ReviewRecord.objects.filter(user=instance.user).count()
    Profile.objects.update_or_create(
    user=instance.user,
    defaults = {
    'last_rating': instance.name,
    'number_rating': count_rating,
    })

##### TEST PAGES #####
class TestEntryModel(models.Model):
    name = models.CharField(max_length=30, default="New", blank=True, null=True)

class TestStoreModel(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

@receiver(post_save, sender=TestEntryModel)
def single_save(sender, instance, **kwargs):
    TestStoreModel.objects.update_or_create(name=instance.name)
