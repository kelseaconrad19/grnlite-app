from django import forms
from .models import Manuscript
from django.utils.translation import gettext_lazy as _

class ManuscriptSubmissionForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = ['title', 'file_path', 'keywords', 'budget', 'beta_readers_needed', 'cover_art', 'nda_required', 'nda_file', 'plot_summary']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'id_title', 
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;'
            }),
            'file_path': forms.FileInput(attrs={
                'class': 'form-control-file', 
                'id': 'id_file_path', 
                'style': 'padding: 5px; background-color: #f9f9f9; border-radius: 5px; margin-bottom: 20px;'
            }),
            'keywords': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input keyword-checkbox', 
                'id': 'id_keywords', 
                'style': 'margin: 10px 0 20px 0;'
            }),
            'budget': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'id_budget', 
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;'
            }),
            'beta_readers_needed': forms.NumberInput(attrs={
                'class': 'form-control', 
                'id': 'id_beta_readers_needed', 
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;'
            }),
            'cover_art': forms.FileInput(attrs={
                'class': 'form-control-file', 
                'id': 'id_cover_art', 
                'style': 'padding: 5px; background-color: #f9f9f9; border-radius: 5px; margin-bottom: 20px;'
            }),
            'nda_required': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'id_nda_required', 
                'style': 'margin: 10px 0 20px 0;'
            }),
            'nda_file': forms.FileInput(attrs={
                'class': 'form-control-file', 
                'id': 'id_nda_file', 
                'style': 'padding: 5px; background-color: #f9f9f9; border-radius: 5px; margin-bottom: 20px;'
            }),
            'plot_summary': forms.Textarea(attrs={
                'class': 'form-control', 
                'id': 'id_plot_summary', 
                'style': 'width: 100%; min-height: 150px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 20px;'
            }),
        }
        labels = {
                "title": _("Title"),
                'file_path': _('Manuscript File'),
                "keywords": _("Genre & Keywords"),
                "budget": _("Budget Per Reader"),
                "beta_readers_needed": _("Number of Beta Readers"),
                "cover_art": _("Cover Art (Optional)"),
                "nda_required": _("Do you want to require an NDA?"),
                "nda_field": _("NDA File (Optional)"),
                "plot_summary": _("Manuscript Plot Summary")
            }
        help_texts = {
            'keywords': None,
            'nda_required': None,
        }
