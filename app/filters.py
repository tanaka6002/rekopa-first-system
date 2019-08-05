from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='メモ欄', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('sex', 'sex'),
        ),
        field_labels={
            'name': '氏名',
            'sex': 'シリーズ',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'memo', 'sex',)
                    #ここの順番を変えると検索画面で項目の順番が変わる。
