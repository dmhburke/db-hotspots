from django.contrib import admin

# Add models
from catalog.models import Profile, MasterAddModel, TestEntryModel, TestStoreModel, CleanReviewModel, SingleLocationRecord, DrinkCreateNewModel, DrinkCreateNewModelDetails, DrinkCreateNewModelFinal #AddReview, SingleLocation, ReviewRecord,

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'userpic', 'homecity', 'number_rating', 'high_rating', 'last_rating',)

# Register the admin class with the associated model
admin.site.register(Profile, ProfileAdmin)

class MasterAddModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating', 'perfect_for', 'city', 'category1', 'category2', 'category3', 'notes', 'postcode', 'suburb', 'date',)

#Register the admin class with the associated model
admin.site.register(MasterAddModel, MasterAddModelAdmin)

##### ADD REVIEW MODEL SET ####

class CleanReviewModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'rating', 'perfect_for', 'city', 'category1', 'category2', 'category3', 'notes', 'postcode', 'suburb', 'date', 'ave_rating','count_rating',)

#Register the admin class with the associated model
admin.site.register(CleanReviewModel, CleanReviewModelAdmin)

class SingleLocationRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'perfect_for', 'city', 'category1', 'category2', 'category3', 'notes', 'postcode', 'suburb', 'date', 'count_ratings', 'count_wishlist', 'ave_ratings',)

#Register the admin class with the associated model
admin.site.register(SingleLocationRecord, SingleLocationRecordAdmin)


##### ADD REVIEW MODEL SET ####



###TEST PAGE
class TestEntryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

#Register the admin class with the associated model
admin.site.register(TestEntryModel, TestEntryModelAdmin)

class TestStoreModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

#Register the admin class with the associated model
admin.site.register(TestStoreModel, TestStoreModelAdmin)


#####DRINK PAGES######
class DrinkCreateNewModelAdmin(admin.ModelAdmin):
    list_display = ('day', 'drinks', 'waters', 'maxBAC', 'date',)

#Register the admin class with the associated model
admin.site.register(DrinkCreateNewModel, DrinkCreateNewModelAdmin)

class DrinkCreateNewModelDetailsAdmin(admin.ModelAdmin):
    list_display = ('day', 'drinks', 'waters', 'maxBAC', 'date',)

#Register the admin class with the associated model
admin.site.register(DrinkCreateNewModelDetails, DrinkCreateNewModelDetailsAdmin)

class DrinkCreateNewModelFinalAdmin(admin.ModelAdmin):
    list_display = ('day', 'drinks', 'waters', 'maxBAC','date','highBAC',)

#Register the admin class with the associated model
admin.site.register(DrinkCreateNewModelFinal, DrinkCreateNewModelFinalAdmin)
