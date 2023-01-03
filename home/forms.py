from django.forms import ModelForm
from home.models import Rohildb
class FormRohil(ModelForm):
    class Meta:
      model = Rohildb
      fields =  "__all__"