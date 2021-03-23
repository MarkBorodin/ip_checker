from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(null=True, auto_now_add=True)
    write_date = models.DateTimeField(null=True, auto_now=True)


class IP(BaseModel):
    address = models.TextField(max_length=64)
    company = models.TextField(max_length=512, null=True)

    class Meta:
        ordering = ["-create_date"]
        verbose_name_plural = "ip addresses"
