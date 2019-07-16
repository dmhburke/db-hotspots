from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

CITIES = (
    ("New York City, NY", "New York City"),
    ("Los Angeles, CA", "Los Angeles"),
    ("Boston, MA", "Boston"),
    ("Seattle, WA", "Seattle"),
    ("Sydney, Australia", "Sydney"),
    ("Stockholm, Sweden", "Stockholm"),
    ("Paris, France", "Paris"),
    ("London, UK", "London"),
)

RATING = (
    ("", "Rating"),
    ("5", "All-time"),
    ("4", "Love it"),
    ("3", "Like it"),
    ("2", "Meh..."),
    ("0", "Skip it!"),
)

PERFECT_FOR = (
    ("Something quick", "Something quick"),
    ("Last-min plans", "Last-min plans"),
    ("Breakfast", "Breakfast"),
    ("Impressing guests", "Impressing guests"),
    ("Date night", "Date night"),
    ("Big group", "Big group"),
    ("Peace & quiet", "Peace & quiet"),
    ("Living large", "Living large"),
    ("Sunny days", "Sunny days"),
    )

SITUATION = (
    ("", "Situation"),
    ("Something quick", "Something quick"),
    ("Last-min plans", "Last-min plans"),
    ("Breakfast", "Breakfast"),
    ("Impressing guests", "Impressing guests"),
    ("Date night", "Date night"),
    ("Big group", "Big group"),
    ("Peace & quiet", "Peace & quiet"),
    ("Living large", "Living large"),
    ("Sunny days", "Sunny days"),
    )


LOCATION = (
    ("", "----"),
    ("Alphabet City", "Alphabet City"),
    ("Astoria", "Astoria"),
    ("Battery Park", "Battery Park"),
    ("Bed-Stuy", "Bed-Stuy"),
    ("Brooklyn Heights", "Brooklyn Heights"),
    ("Central Park", "Central Park"),
    ("Chelsea", "Chelsea"),
    ("Clinton Hill", "Clinton Hill"),
    ("Cobble Hill", "Cobble Hill"),
    ("DUMBO", "DUMBO"),
    ("East Village", "East Village"),
    ("Financial District", "Financial District"),
    ("Fort Greene", "Fort Greene"),
    ("Harlem", "Harlem"),
    ("Hell's Kitchen", "Hell's Kitchen"),
    ("Kips Bay", "Kips Bay"),
    ("Korea Town", "Korea Town"),
    ("Long Island City", "Long Island City"),
    ("Lower East Side", "Lower East Side"),
    ("NoHo", "NoHo"),
    ("NoMad", "NoMad"),
    ("SoHo", "SoHo"),
    ("Times Square", "Times Square"),
    ("Theater District", "Theater District"),
    ("Tribeca", "Tribeca"),
    ("Upper East Side", "Upper East Side"),
    ("West Village", "West Village"),
    ("Williamsburg", "Williamsburg"),
)

CATEGORY = (
    ("", "Type"),
    ("FOOD", "Food"),
    ("COCKTAILS", "Cocktails"),
    ("WINE", "Wine"),
    ("BEER", "Beer"),
    ("COFFEE", "Coffee"),
    ("OTHER", "Other"),
)

CITY = (
    ("", "City"),
    ("New York City, NY", "NYC"),
    ("Los Angeles, CA", "LA"),
    ("Boston, MA", "Boston"),
    ("Seattle, WA", "Seattle"),
    ("Sydney, Australia", "Sydney"),
    ("Stockholm, Sweden", "Stockholm"),
    ("Paris, France", "Paris"),
    ("London, UK", "London"),
)
