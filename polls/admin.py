from django.contrib import admin
from .models import Poll, Choice
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Token, TokenAdmin)

# Register your models here.
