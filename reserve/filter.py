from django_filters import rest_framework as filters
from .models import Reserve


class ReserveFilter(filters.FilterSet):
    class Meta:
        model = Reserve
        fields = [
            'title',
        ]
