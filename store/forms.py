from django import forms
from store.models import ProductReview


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Напишите комментарий'}))

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']