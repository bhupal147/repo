from django import forms
class registrationform(forms.Form):
    first_name=forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter firstname'
            }
        )
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter lastname'
            }
        )
    )
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter username'
            }
        )
    )
    pwd= forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter password'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Mobile No",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter mobile no'
            }
        )
    )
class Loginform(forms.Form):
    username=forms.CharField(
        label="User Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter username'
            }
        )

    )
    pwd = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )

    )