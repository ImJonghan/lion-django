from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label="Search Word")
    # date_val = forms.DateField(label="날짜정보")