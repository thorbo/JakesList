from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from .models import User, Listings, Categories, Comments, Bids

@login_required(login_url="login")
def close(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    listing.active = False
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

@login_required(login_url="login")
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        category = Categories.objects.get(category=request.POST["category"])
        picture = request.POST["picture"]
        price = request.POST["price"]
        expiration = request.POST["expiration"]
        user = User.objects.get(username=request.user.username)
        print("**********************************", user)
        listItem = Listings(title=title, description=description, category=category, picture=picture, price=price, expiration=expiration, lister=user, active=True)
        listItem.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/new.html", {
            "categories": Categories.objects.all()
        })

@login_required(login_url="login")
def watch(request, listing_id):
    listItem = Listings.objects.get(pk=listing_id)
    user = User.objects.get(username=request.user.username)
    user.watchlist.add(listItem)
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

@login_required(login_url="login")
def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Categories.objects.all()
    })

@login_required(login_url="login")
def cat(request, cat_id):
    cat = Categories.objects.get(category=cat_id)
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.filter(category=cat).all()
    })

@login_required(login_url="login")
def watchlist(request):
    user = User.objects.get(username=request.user.username)
    return render(request, "auctions/watchlist.html", {
        "watchlist": user.watchlist.all()
    })

@login_required(login_url="login")
def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.filter(active=True).all()
    })

@login_required(login_url="login")
def listing(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    user = User.objects.get(username=request.user.username)
    print(listing.active)
    if request.method == "POST":
        button = request.POST["subbut"]
        if button == "Comment":
            comment = request.POST["comments"]
            comments = Comments(comment=comment, commenter=user, listing=listing)
            comments.save()
        elif button == "Bid":
            amt = request.POST["bid"]
            BID = Bids(bidder=user, listing=listing, amount=amt)
            BID.save()
            listing.price = amt
            listing.winner = user
            listing.save()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": Comments.objects.filter(listing=listing).all(),
        "lister": user==listing.lister,
        "active": listing.active
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
