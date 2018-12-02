# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Bank(models.Model):
    ifsc_code = models.CharField(max_length=16)
    bank_name = models.CharField(max_length=128)
    branch = models.CharField(max_length=64)
    address = models.TextField()
    city = models.CharField(max_length=64)
    distict = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    bank_id = models.CharField(max_length=8)
