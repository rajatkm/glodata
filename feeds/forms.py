from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, min_length=2, required=True)
    