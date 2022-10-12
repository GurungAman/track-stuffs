from django_filters import rest_framework as filters


class BaseFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    max_price = filters.CharFilter(field_name="status", lookup_expr='iexact')

    class Meta:
        abstract = True
