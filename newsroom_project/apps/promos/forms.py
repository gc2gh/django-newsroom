from django import forms
from promos.models import *
from core.models import *

class PromoForm(forms.ModelForm):
    """
    Create our own form based on the Promo model.  

    We also want to populate the affiliate field with people based on the
    current user making the request.  
    """
    
    #def __init__(self, user=None, *args, **kwargs):
    #    #queryset=Person.objects.filter()
    #    super(PromoForm, self).__init__(*args, **kwargs)
        #person = user.person_set.get()
        #self.fields['authors'].queryset = \
        #    Person.objects.filter(affiate=person.affiliate)
    #     self.fields['permalink'].widget = widgets.TextInput()
    #    #self.fields['authors'].widget = widgets.SelectMultiple()

    headline = forms.CharField(widget=forms.TextInput(attrs={'size':'100'}))
    permalink = forms.CharField(label='URL',widget=forms.TextInput(attrs={'size':'100'}))
    description = forms.CharField(label='Summary / Nut Graph',widget=forms.Textarea(attrs = {'cols':76,'rows':8}))
    other_credits = forms.CharField(required=False,widget=forms.Textarea(attrs = {'cols':40,'rows':3}))
    location = forms.CharField(label='Primary Location',help_text='City, State, Country or ZIP code, Country.',widget=forms.TextInput())

    class Meta:
        model = Promo
        fields = ('headline','permalink','description','authors','other_credits', 'location', 'topic_path')

class LinkForm(forms.ModelForm):

    title = forms.CharField(label='Title/Teaser',widget=forms.TextInput(attrs={'size':'100'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'size':'100'}))
    desc = forms.CharField(help_text='Please provide any related links that might richly supplement the main package/story featured with this promo submission.  They could be from your incubator or another.', widget=forms.Textarea(attrs = {'cols':40,'rows':3}))
   
    class Meta:
        model = PromoLink
        fields = ('title','url','desc')
        
class ImageForm(forms.ModelForm):

    class Meta:
        model = PromoImage
        exclude =('promo')

class DateForm(forms.ModelForm):
    
    class Meta:
        model = PromoDate
        exclude =('promo')

class BillboardForm(forms.ModelForm):
    headline = forms.CharField(widget=forms.TextInput(attrs={'size':'100'}))
    supporting_text = forms.CharField(required=False,widget=forms.Textarea(attrs = {'cols':76,'rows':8}))

    class Meta:
        model = PromoBillboard
        exclude =('promo')

