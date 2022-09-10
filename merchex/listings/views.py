from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from listings.models import Band, Listing
from listings.form import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.form import BandForm


def hello(request: HttpRequest):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {'bands': bands})


def about(request: HttpRequest):
    data = "<h1> A Propos de Charles </h1> <p> Merci d'être passé </p>"
    return HttpResponse(data)


def listings(request: HttpRequest):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {'listings': listings})


def band_list(request: HttpRequest):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands})


def band_detail(request: HttpRequest, band_id):
    band = Band.objects.get(id = band_id)
    return render(request, 'listings/band_detail.html', {"band": band})

def contact(request: HttpRequest):
    print("la méthode de la requête est", request.method)
    print("LEs données de cette requete sont", request.POST)
    if (request.method == 'POST'):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Salut",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data["email"],
                recipient_list=['admin@merchex.xyz'] 
            )
        return redirect('bands')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})



def band_create(request: HttpRequest):
    if (request.method == "POST"):
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html',{'form':form})

def band_update(request: HttpRequest, band_id):
    band = Band.objects.get(id=band_id)

    if (request.method == 'POST'):
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html',{'form': form})


def band_delete(request: HttpRequest, band_id):
    band = Band.objects.get(id = band_id)

    if (request.method == 'POST'):
        band.delete()
        return redirect('bands')

    return render(request, "listings/band_delete.html", {'band': band})