from django.contrib import admin

# Register your models here.

from subapp1.models import Member
from subapp1.models import Account
admin.site.register(Member)
admin.site.register(Account)