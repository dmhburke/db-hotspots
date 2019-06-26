from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

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
    ("", "----"),
    ("FOOD", "Food"),
    ("COCKTAILS", "Cocktails"),
    ("WINE", "Wine"),
    ("BEER", "Beer"),
    ("COFFEE", "Coffee"),
    ("OTHER", "Other"),
)

PERFECT_FOR = (
    ("Something quick", "Something quick"),
    ("Last-min plans", "Last-min plans"),
    ("Impressing guests", "Impressing guests"),
    ("Date night", "Date night"),
    ("Big group", "Big group"),
    ("Peace & quiet", "Peace & quiet"),
    ("Living large", "Living large"),
    ("Sunny days", "Sunny days"),
    )
