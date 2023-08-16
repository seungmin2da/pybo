from django import forms
from pybo.models import Question, Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

