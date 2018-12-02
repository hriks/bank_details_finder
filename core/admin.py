# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("ifsc_code", "bank_name", "city", "state")
    search_fields = ("ifsc_code", "city")
    list_filter = ("state",)
