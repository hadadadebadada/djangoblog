from .models import BlogEntry
from django import forms


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title eingeben"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs=
    {
        "class": "new class name",
        "placeholder": "Beschreibung eingeben",
        "id": "my id for textare",
        "rows": 20,
        "cols": 120

    }))

    class Meta:
        model = BlogEntry
        fields = ["title",
                  "description",]

    ## INPUT VALIDATION
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")  ## getting the cleaned title
        if "SGKS" in title:
            return title
        if not "jojo" in title:
            return title
        else:
            raise forms.ValidationError("Keine Zulaessige Eingabe, bitte mit >SGKS< beginnen")


class RawProductForm(forms.Form):  ##django form fields (google)
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title eingeben"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs=
    {
        "class": "new class name",
        "placeholder": "Beschreibung eingeben",
        "id": "my id for textare",
        "rows": 20,
        "cols": 120

    }))



