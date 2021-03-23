from django.db.models.signals import post_save
from django.dispatch import receiver

from ip_checker.models import IP
from ip_checker.utils import company


@receiver(post_save, sender=IP)
def phase_number(sender, instance, created, **kwargs):
    if created:
        instance.company = company(instance.address)
        instance.save()
