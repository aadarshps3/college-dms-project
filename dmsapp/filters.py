import django_filters
from django.forms import TextInput
from django_filters import CharFilter

from dmsapp.models import Login, Internal_mark


class StudentFilter(django_filters.FilterSet):
    year_of_joining = CharFilter(field_name='year_of_joining',label='',lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Search by Year'}))
    class Meta:
        model = Login
        fields = ('year_of_joining',)

class SubjectFilter(django_filters.FilterSet):
    subject = CharFilter(field_name='subject',label='',lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Search by subject'}))
    class Meta:
        model = Internal_mark
        fields = ('subject',)