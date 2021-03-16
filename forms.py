from django import forms
from .models import Register
from .models import Comment
from .models import Deposit
from .models import WithDraw
from .models import Bill
class Registerform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Registerform, self).__init__(*args, **kwargs)
        self.fields['account'].widget.attrs['readonly'] = True
    class Meta:
        model=Register
        widgets={'Email':forms.EmailInput,'password':forms.PasswordInput}
        fields='__all__'

class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        widgets={'Email':forms.EmailInput,'password':forms.PasswordInput}
        fields='__all__'

class Depositform(forms.ModelForm):
    class Meta:
        model=Deposit
        widgets={'password':forms.PasswordInput}
        fields='__all__'

class WithDrawform(forms.ModelForm):
    class Meta:
        model=WithDraw
        widgets={'password':forms.PasswordInput}
        fields='__all__'

class Billform(forms.ModelForm):
    class Meta:
        model=Bill
        widgets={'password':forms.PasswordInput}
        fields='__all__'
