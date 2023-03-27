from django.contrib import admin

from .models import Bank


class BankAdmin(admin.ModelAdmin):
    list_display = ('id','bank_name', 'slug', 'created', 'updated',)

admin.site.register(Bank, BankAdmin)