from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q, Max
import json, requests
from django.contrib.gis.geoip2 import GeoIP2
from django.urls import reverse
from hotSpotsApp.settings import *
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
from catalog.choices import *

#Import User model here
from django.contrib.auth.models import User

#Import Custom models here
from catalog.models import Profile, TestEntryModel, TestStoreModel, MasterAddModel, CleanReviewModel, SingleLocationRecord, DrinkCreateNewModel, DrinkCreateNewModelDetails, DrinkCreateNewModelFinal #AddReview, SingleLocation, ReviewRecord,

#Import forms here
from catalog.forms import ProfileForm, SpotFinderForm, TestEntryForm, MasterAddForm, DrinkCreateNewForm, DrinkCreateNewDetailsForm #AddReviewForm,

#DEFINE VIEWS HERE
def createaccount (request):
    """Create user account"""
# Add view details here
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.userpic = form.cleaned_data.get('userpic')
            user.profile.homecity = form.cleaned_data.get('homecity')
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = ProfileForm()

    return render(request, 'createaccount.html', {'form': form})

@login_required
def home (request):
    """Home page for form entry"""
    # Add view details here
    if request.method == 'POST':
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('userspotlist') #or whatever the url
    else:
        form = AddReviewForm()

    context = {
        'form': form,
    }
    return render(request, 'home.html', context=context)

@login_required
def landingadd(request):

    logged_in_user = request.user
    user_city = logged_in_user.profile.homecity

    search_result = {}
    if 'name' in request.POST:
          form = TestEntryForm(request.POST)
          if form.is_valid():
              search_result = form.search(request)
    else:
          form = TestEntryForm(initial={'city': user_city})

    context={
    'form': form,
    'search_result': search_result,
    }

    return render(request, 'landingadd.html', context=context)

@login_required
def adddetail(request, name, lat, lng):

####FOURSQUARE API####
    lat = lat
    long = lng
    targetLocation = str(lat) + ', ' + str(long)

    detailsURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
    detailsParams = dict(
        client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
        client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
         v='20180323',
         ll=targetLocation,
         query=name,
         limit=10,
         )
    detailsResponse = requests.get(url=detailsURL, params=detailsParams)
    detailsData = detailsResponse.json()
    detailsStatus = detailsResponse.status_code
    detailsInfo = json.loads(detailsResponse.text)

    detailsResult = detailsInfo['response']['minivenues'][0]
    resultName = detailsResult['name']
    try:
        resultAddress = detailsResult['location']['address']
    except:
        resultAddress = ''
    try:
        resultCity = detailsResult['location']['city']
    except:
        resultCity = ''
    try:
        resultCountry = detailsResult['location']['country']
    except:
        resultCountry = ''
    try:
        resultCategory1 = detailsResult['categories'][0]['name']
    except:
        resultCategory1 = ""
    try:
        resultCategory2 = detailsResult['categories'][1]['name']
    except:
        resultCategory2 = ""
    try:
        resultCategory3 = detailsResult['categories'][2]['name']
    except:
        resultCategory3 = ""
    try:
        resultPostcode = detailsResult['location']['postalCode']
    except:
        resultPostcode = ""

    imageQuery = resultName + " " + resultAddress

####GOOGLE IMAGE API ######
    searchURL = 'https://www.googleapis.com/customsearch/v1'
    searchParams = dict(
        cx=google_project_cx,
        key=google_dev_api_key,
        q=imageQuery,
        searchType='image',
        fileType='.jpg',
        num=6,
    )

    searchResponse = requests.get(url=searchURL, params=searchParams)
    searchStatus = searchResponse.status_code
    searchData = searchResponse.json()
    searchInfo = json.loads(searchResponse.text)

    try:
        imageResult = searchInfo['items']
    except:
        imageResult = None

###ADD ADDITIONAL LOCATION DETAILS####
    key = 'a98d10680c0c41d082d9de1c23dcec22'
    geocoder = OpenCageGeocode(key)

    locationResponse = geocoder.reverse_geocode(lat, long)

    try:
        resultSuburb = locationResponse[0]['components']['suburb']
    except:
        resultSuburb = ''

####FORM FOR USERS INPUTS ####
    if request.method == 'POST':
        form = MasterAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.name = resultName
            post.city = resultCity
            post.category1 = resultCategory1
            post.category2 = resultCategory2
            post.category3 = resultCategory3
            post.postcode = resultPostcode
            post.suburb = resultSuburb
            post.save()
            return redirect('browsespots') #or whatever the url
    else:
        form = MasterAddForm()

    context = {
    'form': form,
    'name': name,
    'targetLocation': targetLocation,
    'detailsData': detailsData,
    'resultName': resultName,
    'resultCity': resultCity,
    'resultCountry': resultCountry,
    'resultAddress': resultAddress,
    'resultCategory1': resultCategory1,
    'resultCategory2': resultCategory2,
    'resultCategory3': resultCategory3,
    'resultPostcode': resultPostcode,
    'searchStatus': searchStatus,
    'imageResult': imageResult,
    'searchData': searchData,
    'resultSuburb': resultSuburb,
    }

    return render(request, 'adddetail.html', context=context)

@login_required
def findspot (request):

##Define user and city
    logged_in_user = request.user
    user_city = logged_in_user.profile.homecity

    situation_result = {}
    category_result = {}
    location_result = {}
    # source_result = {}

    if request.method =='POST':
         form = SpotFinderForm(request.POST)
         if form.is_valid():
             category_result = form.category_query(request)
             situation_result = form.situation_query(request)
             location_result = form.location_query(request)
             # source_result = form.source_query(request)
    else:
          form = SpotFinderForm(initial={
          'location': user_city,
          })

## -- LOCATION RESULTS --
    postcode_result1 = {}
    postcode_result2 = {}
    postcode_result3 = {}
    postcode_result4 = {}

    if location_result == "Los Angeles, CA":
        postcode_result1 = 90
        postcode_result2 = 90
        postcode_result3 = 90
        postcode_result4 = 90
    elif location_result == "New York City, NY":
        postcode_result1 = 1
        postcode_result2 = 1
        postcode_result3 = 1
        postcode_result4 = 1
    elif location_result == "London, UK":
        postcode_result1 = "N"
        postcode_result2 = "E"
        postcode_result3 = "W"
        postcode_result4 = "S"
    elif location_result == "Seattle, WA":
        postcode_result1 = 98
        postcode_result2 = 98
        postcode_result3 = 98
        postcode_result4 = 98
    elif location_result == "Sydney, Australia":
        postcode_result1 = 20
        postcode_result2 = 21
        postcode_result3 = 22
        postcode_result4 = 25
    else:
        postcode_result1 = ""
        postcode_result2 = ""
        postcode_result3 = ""
        postcode_result4 = ""

## -- TYPE RESULTS --

    optioncategory1_result = {}
    optioncategory2_result = {}
    optioncategory3_result = {}

    if category_result == "FOOD":
        optioncategory1_result = "Restaurant"
        optioncategory2_result = "Food"
        optioncategory3_result = "Café"
    elif category_result == "COFFEE":
        optioncategory1_result = "Café"
        optioncategory2_result = "Coffee shop"
        optioncategory3_result = "Coffee shop"
    elif category_result == "WINE":
        optioncategory1_result = "Wine"
        optioncategory2_result = "Wine"
        optioncategory3_result = "Wine"
    elif category_result == "BEER":
        optioncategory1_result = "Beer"
        optioncategory2_result = "Pub"
        optioncategory3_result = "Gastropub"
    elif category_result == "COCKTAILS":
        optioncategory1_result = "Cocktail"
        optioncategory2_result = "Bar"
        optioncategory3_result = "Nightlife"
    else:
        optioncategory1_result = ""
        optioncategory2_result = ""
        optioncategory3_result = ""

## - SEARCH RESULT --

    spot_finder = SingleLocationRecord.objects.filter(
               (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
               Q(perfect_for__contains=situation_result) &
               (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)
               )).order_by('-ave_ratings', 'count_ratings')

    your_rating = CleanReviewModel.objects.filter(user=request.user)

## -- SOURCE RESULT -- [DORMANT]

    # name_output = {}
    # rating_output = {}
    #
    # if source_result == "MINE":
    #     name_output = logged_in_user
    #     rating_output = ""
    # elif source_result == "WISHLIST":
    #     name_output = logged_in_user
    #     rating_output = ""
    # # elif source_result == "EVERYTHING":
    # #     name_output = "Everyone else"
    # #     rating_output = "Anything"
    # elif source_result == "SUGGESTED":
    #     name_output = "Everyone else"
    #     rating_output = 4
    # else:
    #     name_output = "No selection"
    #     rating_output = "Anything"
    #
    # if source_result == "MINE":
    #      spot_finder = CleanReviewModel.objects.filter(
    #         (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
    #         Q(perfect_for__contains=situation_result) &
    #         ~Q(rating=rating_output) &
    #         (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)) &
    #         Q(user__username__contains=name_output)
    #         ).order_by('-rating')
    # elif source_result == "WISHLIST":
    #      spot_finder = CleanReviewModel.objects.filter(
    #         (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
    #         (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)) &
    #         Q(user__username__contains=name_output) &
    #         Q(rating=rating_output)
    #         ).order_by('-date')
    # # elif source_result == "EVERYTHING":
    # #      spot_finder = MasterAddModel.objects.filter(
    # #         (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
    # #         Q(perfect_for__contains=situation_result) &
    # #         (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)
    # #         )).exclude(user__username=logged_in_user
    # #         ).order_by('-rating')
    #
    # #####NEED TO BUILD FOR LOOP TO FIND RIGHT ENTRIES ######
    # elif source_result == "SUGGESTED":
    #     spot_finder = SingleLocationRecord.objects.filter(
    #     (Q(postcode__startswith=postcode_result1) | Q(postcode__startswith=postcode_result2) | Q(postcode__startswith=postcode_result3) | Q(postcode__startswith=postcode_result4)) &
    #     Q(perfect_for__contains=situation_result) &
    #     (Q(category1__contains=optioncategory1_result) | Q(category1__contains=optioncategory2_result) | Q(category1__contains=optioncategory3_result)) &
    #     Q(ave_ratings__gte=rating_output)
    #     #).exclude(user__username=logged_in_user
    #     #).distinct('name'
    #     ).order_by('-ave_ratings', '-date')
    #
    #     # user_been = CleanReviewModel.objects.filter(user=request.user)


    context = {
    'form': form,
    'spot_finder': spot_finder,
    # 'name_output': name_output,
    'postcode_result': postcode_result1,
    'optioncategory1_result': optioncategory1_result,
    'situation_result': situation_result,
    'logged_in_user': logged_in_user,
    'your_rating': your_rating,
    }

    return render(request, 'findspots.html', context=context)

@login_required
def browsespots(request):
    """View to browse yours, wishlist and activity"""

    activity_stream = CleanReviewModel.objects.all().order_by('-date')

    your_spots = CleanReviewModel.objects.filter(user=request.user, rating__gte=0).order_by("-rating", "-date")

    your_wishlist = CleanReviewModel.objects.filter(user=request.user, rating="").order_by("-date")

    context={
    'activity_stream': activity_stream,
    'your_spots': your_spots,
    'your_wishlist': your_wishlist,

    }

    return render(request,'browsespots.html', context=context)


@login_required
def userspotlist(request):
    """Create view to see your own spots"""
    user_hitlist = ReviewRecord.objects.filter(user=request.user, rating__isnull=False).order_by('-rating')
    user_wishlist = ReviewRecord.objects.filter(user=request.user, rating__isnull=True).order_by('-date')

    context = {
    'user_hitlist': user_hitlist,
    'user_wishlist': user_wishlist,
    }

    return render(request, 'userpage.html', context=context)

@login_required
def userspotdetail(request,pk):
    """Create spot detail for user entry"""

    spotname = SingleLocation.objects.get(name=pk)
    spotlocation = SingleLocation.objects.get(name=pk).location
    spot_averating = SingleLocation.objects.get(name=pk).averating
    spot_rating = ReviewRecord.objects.filter(name=pk)
    fullspot_rating = AddReview.objects.filter(name=pk).order_by('date')
    spot_img = ReviewRecord.objects.filter(name=pk).exclude(spotpic='')
    number_hitlist = AddReview.objects.filter(name=pk).exclude(rating=None).count()
    number_wishlist = AddReview.objects.filter(name=pk, rating=None).count()


# Define HTML context
    context = {
        'spotname': spotname,
        'spotlocation': spotlocation,
        'spot_rating': spot_rating,
        'fullspot_rating': fullspot_rating,
        'spot_averating': spot_averating,
        'spot_img': spot_img,
        'number_hitlist': number_hitlist,
        'number_wishlist': number_wishlist,
    }

    return render(request, 'userspotdetail.html', context=context)

@login_required
def userdetail (request, pk):
    """Create user detail for user entry"""
    userpic = Profile.objects.get(user__username=pk).userpic
    userfirstname = User.objects.get(username=pk).first_name
    userlastname = User.objects.get(username=pk).last_name
    userusername = User.objects.get(username=pk).username
    countrating = ReviewRecord.objects.filter(user__username=pk).exclude(rating=None).count()
    sumrating = list(ReviewRecord.objects.filter(user__username=pk).aggregate(Sum('rating')).values())[0]
    try:
        averating = sumrating / countrating
    except:
        averating = None


    count_wishlist = ReviewRecord.objects.filter(user__username=pk, rating=None).count()
    count_hitlist = ReviewRecord.objects.filter(user__username=pk).exclude(rating=None).count()
    user_list = ReviewRecord.objects.filter(user__username=pk).order_by('-date')

    food_adds = ReviewRecord.objects.filter(user__username=pk, category="FOOD").count()
    beer_adds = ReviewRecord.objects.filter(user__username=pk, category="BEER").count()
    wine_adds = ReviewRecord.objects.filter(user__username=pk, category="WINE").count()
    cocktail_adds = ReviewRecord.objects.filter(user__username=pk, category="COCKTAILS").count()
    coffee_adds = ReviewRecord.objects.filter(user__username=pk, category="COFFEE").count()
    other_adds = ReviewRecord.objects.filter(user__username=pk, category="OTHER").count()

    drink_adds = beer_adds + wine_adds + cocktail_adds
    all_adds = drink_adds + food_adds + coffee_adds + other_adds
    try:
        food_pct = food_adds / all_adds *100
    except:
        food_pct = None
    try:
        drink_pct = drink_adds / all_adds*100
    except:
        drink_pct = None
    try:
        coffee_pct = coffee_adds / all_adds*100
    except:
        coffee_pct = None
    try:
        other_pct = other_adds / all_adds*100
    except:
        other_pct = None

    userdetail_hitlist = ReviewRecord.objects.filter(user__username=pk, rating__isnull=False).order_by('-rating')
    userdetail_wishlist = ReviewRecord.objects.filter(user__username=pk, rating__isnull=True).order_by('-date')



    context = {
    'userpic': userpic,
    'userfirstname': userfirstname,
    'userlastname': userlastname,
    'userusername': userusername,
    'food_adds': food_adds,
    'drink_adds': drink_adds,
    'coffee_adds': coffee_adds,
    'other_adds': other_adds,
    'food_pct': food_pct,
    'drink_pct': drink_pct,
    'coffee_pct': coffee_pct,
    'other_pct': other_pct,
    'averating': averating,
    'count_hitlist': count_hitlist,
    'count_wishlist': count_wishlist,
    'userdetail_hitlist': userdetail_hitlist,
    'userdetail_wishlist': userdetail_wishlist,
    }

    return render(request, 'userdetail.html', context=context)

@login_required
def activitystream (request):
    """See all users' activity """
# Add view details here

    activity_stream = AddReview.objects.all().order_by('-date')

    context = {
    "activity_stream": activity_stream,
    }
    return render(request, 'activitystream.html', context=context)

@login_required
def discovernew (request):
    """Page for deep dive into users and spots"""
    single_spot_list = SingleLocation.objects.all().order_by('name')
    user_list = Profile.objects.all().order_by('user')
    high_rating = list(AddReview.objects.aggregate(Max('rating')).values())[0]

    try:
        high_rating_name = AddReview.objects.get(rating=high_rating).name
    except:
        high_rating_name = "None added"

    context={
    'single_spot_list': single_spot_list,
    'user_list': user_list,
    'high_rating_name': high_rating_name,
    'high_rating': high_rating,
    }

    return render(request, 'discovernew.html', context=context)



##### TEST PAGE ####
#FourSquare Developer API: https://foursquare.com/developers/apps/0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35/settings
def testpage (request):
    """use for any testing needed"""

    # logged_in_user = request.user
    # user_city = logged_in_user.profile.location
    #
    # search_result = {}
    # if 'name' in request.POST:
    #       form = TestEntryForm(request.POST)
    #       if form.is_valid():
    #           search_result = form.search(request)
    # else:
    #       form = TestEntryForm(initial={'city': user_city})
    #
    # #CODE TO SHOW FULL JSON (not linked to search)
    # completeURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
    # completeParams = dict(
    #     client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
    #      client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
    #      v='20180323',
    #      ll='40.734581,-74.003860',
    #      query=search_result,
    #      limit=1,)
    # completeResponse = requests.get(url=completeURL, params=completeParams)
    # completeStatus = completeResponse.status_code
    # completeDetails = completeResponse.content
    # completeData = completeResponse.json()
    # #NONE OF ABOVE REFRENCES SEARCH
    #
    context={
    # 'form': form,
    # 'search_result': search_result,
    # 'completeData': completeData,
    # # 'searchQuery': searchQuery,
    # # 'searchStatus': searchStatus,
    # # 'searchDetails': searchDetails,
    # # 'searchData': searchData,
    # # 'completeStatus': completeStatus,
    # # 'completeQuery': completeQuery,
    # # 'completeData': completeData,
    #
        }

    return render(request, 'testpage.html', context=context)

# def testpagedetail (request, name, lat, lng):
#     """use for any testing links needed"""
#
#     name=name
#     lat = lat
#     long = lng
#     targetLocation = str(lat) + ', ' + str(long)
#
#     detailsURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
#     detailsParams = dict(
#         client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
#         client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
#          v='20180323',
#          ll=targetLocation,
#          query=name,
#          limit=10,
#          )
#     detailsResponse = requests.get(url=detailsURL, params=detailsParams)
#     detailsData = detailsResponse.json()
#     detailsStatus = detailsResponse.status_code
#     detailsInfo = json.loads(detailsResponse.text)
#
#     detailsResult = detailsInfo['response']['minivenues'][0]
#     resultName = detailsResult['name']
#     resultAddress = detailsResult['location']['address']
#     resultCity = detailsResult['location']['city']
#     resultCountry = detailsResult['location']['country']
#     try:
#         resultCategory1 = detailsResult['categories'][0]['name']
#     except:
#         resultCategory1 = ""
#     try:
#         resultCategory2 = detailsResult['categories'][1]['name']
#     except:
#         resultCategory2 = ""
#     try:
#         resultCategory3 = detailsResult['categories'][2]['name']
#     except:
#         resultCategory3 = ""
#     try:
#         resultPostcode = detailsResult['location']['postalCode']
#     except:
#         resultPostcode = ""
#
#     #ADD GOOGLE IMAGES SEARCH
#     #googleDevAPIKey = 'AIzaSyArd-i81wSGtCnJxDCFdBD0jrvX8AXOsCc'
#     #googleProjectCX = '000959550691752782256:tckrhqdefn8'
#
#     imageQuery = resultName + " " + resultAddress
#
#     searchURL = 'https://www.googleapis.com/customsearch/v1'
#     searchParams = dict(
#         cx=google_project_cx,
#         key=google_dev_api_key,
#         q=imageQuery,
#         searchType='image',
#         fileType='.jpg',
#         num=6,
#     )
#
#     searchResponse = requests.get(url=searchURL, params=searchParams)
#     searchStatus = searchResponse.status_code
#     searchData = searchResponse.json()
#     searchInfo = json.loads(searchResponse.text)
#
#     # try:
#     #     imageResult1 = searchInfo['items'][0]['link']
#     # except:
#     #     imageResult1 = "None"
#
#     imageResult = searchInfo['items']
#
#     jsonExplore = "None"
#
#     ###OpenCageLatLong2SmartLocation###
#
#     # locationURL =
#     # locationParams = dict (
#     #
#     # )
#
#     key = 'a98d10680c0c41d082d9de1c23dcec22'
#     geocoder = OpenCageGeocode(key)
#
#     locationResponse = geocoder.reverse_geocode(lat, long)
#     resultSuburb = locationResponse[0]['components']['suburb']
#
#
#
#     ####FORM FOR USERS INPUTS ####
#     if request.method == 'POST':
#         form = MasterAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.name = resultName
#             post.city = resultCity
#             post.category1 = resultCategory1
#             post.category2 = resultCategory2
#             post.category3 = resultCategory3
#             post.postcode = resultPostcode
#             post.suburb = resultSuburb
#             post.save()
#             return redirect('testpage') #or whatever the url
#     else:
#         form = MasterAddForm()
#
#
#
#     context = {
#     'form': form,
#     'name': name,
#     'targetLocation': targetLocation,
#     'detailsData': detailsData,
#     'resultName': resultName,
#     'resultCity': resultCity,
#     'resultCountry': resultCountry,
#     'resultAddress': resultAddress,
#     'resultCategory1': resultCategory1,
#     'resultCategory2': resultCategory2,
#     'resultCategory3': resultCategory3,
#     'resultPostcode': resultPostcode,
#     'searchStatus': searchStatus,
#     'imageResult': imageResult,
#     'searchData': searchData,
#     'jsonExplore': jsonExplore,
#     'resultSuburb': resultSuburb,
#     }
#
#     return render(request, 'testpagedetail.html', context=context)

def spotfulldetail(request, name, city):

    # IMAGE CAROUSEL
    imageQuery = name + " " + city


    searchURL = 'https://www.googleapis.com/customsearch/v1'
    searchParams = dict(
        cx=google_project_cx,
        key=google_dev_api_key,
        q=imageQuery,
        searchType='image',
        fileType='.jpg',
        num=6,
    )

    searchResponse = requests.get(url=searchURL, params=searchParams)
    searchStatus = searchResponse.status_code
    searchData = searchResponse.json()
    searchInfo = json.loads(searchResponse.text)

    imageResult = searchInfo['items']

    #REVIEW DETAILS
    numberVisits = CleanReviewModel.objects.filter(name=name).exclude(user=request.user).count()
    numberReviews = MasterAddModel.objects.filter(name=name)
    countRatings = CleanReviewModel.objects.filter(name=name).exclude(rating="").count()

    #SUMDETAILS
    sum5Ratings = CleanReviewModel.objects.filter(name=name, rating='5').count()*5
    sum4Ratings = CleanReviewModel.objects.filter(name=name, rating='4').count()*4
    sum3Ratings = CleanReviewModel.objects.filter(name=name, rating='3').count()*3
    sum2Ratings = CleanReviewModel.objects.filter(name=name, rating='2').count()*2
    sum1Ratings = CleanReviewModel.objects.filter(name=name, rating='1').count()*1

    sumRatings = sum5Ratings + sum4Ratings + sum3Ratings + sum2Ratings + sum1Ratings
    try:
        aveRating = sumRatings/countRatings
    except:
        aveRating = "None"

    context = {
    'name': name,
    'city': city,
    'imageResult': imageResult,
    'numberReviews': numberReviews,
    'numberVisits': numberVisits,
    'countRatings': countRatings,
    'aveRating': aveRating,

    }

    return render(request, 'spotfulldetail.html',context=context)



    ####### DRINKS ########

def drinkoverview(request):
    """Frontpage"""
    if request.method == 'POST':
        form = DrinkCreateNewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('drinkoverview')
    else:
        form = DrinkCreateNewForm()

    listDays = DrinkCreateNewModelFinal.objects.all().order_by('-date')

    context = {
    'form': form,
    'listDays': listDays,
    }

    return render(request, 'XXdrinkoverview.html', context=context)

def drinkentry(request, day):
    """Enter details of drinks and save to DB"""

    day = day
    date_created = DrinkCreateNewModel.objects.get(day=day).date

    if request.method == 'POST':
        form = DrinkCreateNewDetailsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.day = day
            post.date = date_created
            post.save()
            return redirect('drinkoverview')
    else:
        try:
            form = DrinkCreateNewDetailsForm(instance=get_object_or_404(DrinkCreateNewModelFinal,day=day))
        except:
            form = DrinkCreateNewDetailsForm()

    context = {
    'day': day,
    'form': form,
    }

    return render(request, 'XXdrinkentry.html', context=context)
