from django import forms


class SectionForm(forms.ModelForm):
	name = forms.CharField()
	image_path = forms.CharField(max_length=255, label='Select a Image File')