from django.db import models
from django.core import validators


class Item(models.Model):

    SERIES_CHOICES = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (11, 'XI'),
        (12, 'XII'),
        (13, 'XIII'),
        (14, 'XIV'),
        (15, 'XV'),
        (16, 'T'),
        (17, '零'),
        (18, 'KH'),
        (19, '外伝'),
        (20, 'Job'),
    )

    name = models.CharField(verbose_name='名前', max_length=200,)
    memo = models.TextField(verbose_name='メモ欄', max_length=1000, blank=True, null=True,)
    sex = models.IntegerField(verbose_name='シリーズ', choices=SERIES_CHOICES, default=1,)
    created_at = models.DateTimeField(verbose_name='登録日', auto_now_add=True,)
    #age = models.IntegerField(verbose_name='シリーズ', validators=[validators.MinValueValidator(1)], blank=True, null=True,)

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'