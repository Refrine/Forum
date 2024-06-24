from django.forms import ModelForm
from .models import Forum

class RoomForm(ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'