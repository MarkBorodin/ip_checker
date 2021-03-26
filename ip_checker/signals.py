from django.db.models.signals import post_save
from django.dispatch import receiver

from ip_checker.models import IP
from ip_checker.utils import get_other_information, get_host, get_ptr


@receiver(post_save, sender=IP)
def process_ip(sender, instance, created, **kwargs):
    if created:
        instance.host = get_host(instance.address)
        result = get_other_information(instance.address)
        instance.PTR_record = get_ptr(instance.address)
        instance.company = result['company']
        instance.ip_range = result['range']
        instance.city = result['city']
        instance.description = result['description']
        instance.asn_description = result['asn_description']
        instance.real_address = result['real_address']
        instance.country = result['country']
        instance.emails = result['emails']
        instance.save()
