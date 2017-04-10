from itertools import chain
from django.db.models import Q
from rest_framework import viewsets, mixins, generics 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Offer
from .serializers import OfferSerializer,OfferSearchSerializer,OfferSearchUserSerializer

class OfferViewSet(viewsets.ModelViewSet): 
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferSearchList(generics.ListAPIView):
    serializer_class = OfferSearchSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)   

        offer = Offer.objects.filter( 
            Q(title__icontains=query) | Q(author__icontains=query)
        )

        all_results = list(chain(offer))
        return all_results


class OfferSearchUserList(generics.ListAPIView):
    serializer_class = OfferSearchUserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)   

        offer = Offer.objects.filter( 
            owner = query,
        )

        all_results = list(chain(offer))
        return all_results

