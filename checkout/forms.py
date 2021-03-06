from django import forms
from .models import Order, OrderLineItem


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(j, j) for j in range(2019, 2029)]

    credit_card_number = forms.CharField(
                                         label='Credit Card Number:',
                                         required=False)
    cvv = forms.CharField(
                          label='Security code (CVV): ',
                          required=False)
    expiry_month = forms.ChoiceField(
                                     label="Month",
                                     choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(
                                    label='Year',
                                    choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode',
                  'city_or_town', 'address1', 'address2', 'county')
