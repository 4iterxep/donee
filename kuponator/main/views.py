from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kuponi, Basket


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def kupons(request):
    kupons = Kuponi.objects.order_by('title')
    return render(request, 'main/kupons.html', {'kupons': kupons})

@login_required
def profile(request):
    baskets = Basket.objects.filter(user=request.user)
    return render(request, 'main/profile.html', context={'baskets': baskets})

class KuponDetailView(DetailView):
    model = Kuponi
    template_name = 'main/detail_view.html'
    context_object_name = 'kupon'

class SearchResultsView(ListView):
    model = Kuponi
    template_name = 'main/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q'.lower())
        object_list = Kuponi.objects.filter(
            Q(title=query)
        )
        return object_list


def basket_add(request, kupon_id):
    kuponi = Kuponi.objects.get(id=kupon_id)
    baskets = Basket.objects.filter(user=request.user, products=kuponi)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=kuponi, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity == 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))