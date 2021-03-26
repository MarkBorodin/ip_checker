from django.contrib import admin
from django.forms import Textarea

from ip_checker.models import IP, models


class IPAdmin(admin.ModelAdmin):
    model = IP
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }
    list_display = (
        'address', 'company', 'host', 'PTR_record', 'ip_range',
        'description', 'asn_description',  'real_address',  'country',  'city', 'emails'
    )
    search_fields = (
        'address', 'company', 'host', 'PTR_record', 'ip_range',
        'description', 'asn_description',  'real_address',  'country',  'city', 'emails'
    )
    # list_filter = (
    #     'address', 'company', 'host', 'PTR_record', 'ip_range',
    #     'description', 'asn_description', 'real_address', 'country', 'city', 'emails'
    # )
    fields = (
        'address',
    )


admin.site.register(IP, IPAdmin)
