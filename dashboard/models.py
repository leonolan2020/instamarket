from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _
# Create your models here.
class MainSlider(models.Model):
    title=models.CharField(_("title"), max_length=50)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    date_edited=models.DateTimeField(_("date_edited"), auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = _("MainSlider")
        verbose_name_plural = _("MainSliders")

    def __str__(self):
        return f'{self.title} {self.date_added} {self.date_edited}'

    def get_absolute_url(self):
        return reverse("MainSlider_detail", kwargs={"pk": self.pk})
