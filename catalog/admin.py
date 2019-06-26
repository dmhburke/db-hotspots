from django.contrib import admin

# Add models
from catalog.models import Profile, AddReview, SingleLocation, ReviewRecord, TestEntryModel, TestStoreModel

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'userpic', 'location', 'number_rating', 'high_rating', 'last_rating',)

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

# Register your models here.
class AddReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location', 'category', 'spotpic', 'perfect_for', 'notes', 'rating', 'date',)

#Register the admin class with the associated model
admin.site.register(AddReview, AddReviewAdmin)

class SingleLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'category', 'countrating', 'averating', 'load_image', 'perfect_for',)

#Register the admin class with the associated model
admin.site.register(SingleLocation, SingleLocationAdmin)

class ReviewRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location', 'category', 'rating',)

#Register the admin class with the associated model
admin.site.register(ReviewRecord, ReviewRecordAdmin)




###TEST PAGE
class TestEntryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

#Register the admin class with the associated model
admin.site.register(TestEntryModel, TestEntryModelAdmin)

class TestStoreModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

#Register the admin class with the associated model
admin.site.register(TestStoreModel, TestStoreModelAdmin)
