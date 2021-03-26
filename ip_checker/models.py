from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(null=True, auto_now_add=True)
    write_date = models.DateTimeField(null=True, auto_now=True)


class IP(BaseModel):
    address = models.TextField(max_length=64)
    company = models.TextField(max_length=1024, null=True)
    PTR_record = models.TextField(max_length=1024, null=True)
    ip_range = models.TextField(max_length=1024, null=True)
    host = models.TextField(max_length=1024, null=True)
    description = models.TextField(max_length=1024, null=True)
    asn_description = models.TextField(max_length=1024, null=True)
    real_address = models.TextField(max_length=1024, null=True)
    country = models.TextField(max_length=128, null=True)
    city = models.TextField(max_length=128, null=True)
    emails = models.TextField(max_length=128, null=True)

    class Meta:
        ordering = ["-create_date"]
        verbose_name_plural = "ip addresses"
