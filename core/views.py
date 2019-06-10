# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions, generics
from core.serializers import BankSerializer, Bank
from rest_framework.filters import (
    SearchFilter, OrderingFilter)


class GetIFSCBankDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    lookup_field = "ifsc_code"


class GetBankDetails(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BankSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['bank_name']

    def get_queryset(self):
        queryset = Bank.objects.all()
        #queryset = Bank.objects.filter(
        #    city__icontains=self.kwargs.get('city')
        #)
        if "bank_name" in self.request.query_params:
            queryset = queryset.filter(
                bank_name__icontains=self.request.query_params['bank_name'])
        return queryset
