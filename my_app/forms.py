from django import forms
from .models import Manuscript
from django.utils.translation import gettext_lazy as _

class ManuscriptSubmissionForm(forms.ModelForm):
    class Meta:
        model = Manuscript
        fields = ['title', 'file_path', 'keywords', 'budget', 'beta_readers_needed', 'cover_art', 'nda_required', 'nda_file', 'plot_summary']
        widgets = {
            'nda_required': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_nda_required'}),
            'nda_file': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'id_nda_file'}),
            'keywords': forms.CheckboxSelectMultiple(),
            'plot_summary': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
                "title": _("Title"),
                'file_path': _('Manuscript File'),
                "keywords": _("Genre & Keywords"),
                "budget": _("Budget Per Reader"),
                "beta_readers_needed": _("Number of Beta Readers"),
                "cover_art": _("Cover Art (Optional)"),
                "nda_required": _("Require NDA"),
                "nda_field": _("NDA File (Optional)"),
                "plot_summary": _("Manuscript Plot Summary")
            }
