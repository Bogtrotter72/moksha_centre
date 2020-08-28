from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'country', 'postcode')
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the 'full_name' field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email address',
            'street_address1': 'Address line 1',
            'street_address2': 'Address line 2',
            'town_or_city': 'Town or city',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postal or zip code',
        }

        # Set autofocus
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Iterate through the fields
        for field in self.fields:
            # Add an asterisk to the placeholder text in required fields
            # If this does not work use self.fields[field] instead
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False