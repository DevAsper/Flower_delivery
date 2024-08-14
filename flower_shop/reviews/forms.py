# apps/reviews/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.Select(choices=Review.RATING_CHOICES),
        }
