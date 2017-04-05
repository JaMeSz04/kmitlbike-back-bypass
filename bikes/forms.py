from django import forms


class BikeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BikeForm, self).__init__(*args, **kwargs)

    TRUE_FALSE_CHOICES = (
        (True, "Yes"),
        (False, "No"),
    )

    is_available = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, widget=forms.Select)
