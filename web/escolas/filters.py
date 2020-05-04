from django_filters import rest_framework as filters


class CeuFilter(filters.FilterSet):
    dre = filters.CharFilter(method='get_dre', field_name='nm_unidade_administrativa')

    def get_dre(self, q, fieldname, value):
        if value:
            value = f'DRE - {value}'
            return q.filter(nm_unidade_administrativa=value)
        return q
