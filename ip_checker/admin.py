from django.contrib import admin
from django.forms import Textarea

from ip_checker.models import IP, models


class IPAdmin(admin.ModelAdmin):
    model = IP
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }
    list_display = (
        'address', 'company'
    )
    search_fields = (
        'address', 'company'
    )
    list_filter = (
        'address', 'company'
    )
    fields = (
        'address',
    )


admin.site.register(IP, IPAdmin)
