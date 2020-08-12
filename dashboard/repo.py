from .models import MainSlider


class MainSliderRepo:
    def __init__(self, *args, **kwargs):
        self.objects=MainSlider.objects
    def list(self,*args, **kwargs):
        return self.objects.all()
