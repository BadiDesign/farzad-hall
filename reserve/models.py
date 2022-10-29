import datetime

from badi_ticket.models import file_size
from badi_utils.dynamic_models import BadiModel
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import Manager

User = get_user_model()


class Reserve(models.Model):
    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو ها'
        permissions = (
            ('can_reserve', 'مدیریت رزرو ها'),
        )
        ordering = ['-id']

    title = models.CharField(max_length=100, null=True, verbose_name='عنوان', )
    reserve_date = models.DateField(verbose_name="تاریخ")
    reserve_time = models.TimeField(verbose_name="ساعت")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ایجاد')
    description = models.TextField(validators=[MaxLengthValidator(1000)], verbose_name="توضیحات")

    # subtitle = models.FileField(null=True, blank=True, upload_to='media/subtitles/', verbose_name='فایل زیرنویس vtt')

    def __str__(self):
        return self.title

    @staticmethod
    def get_datatable_columns():
        return ['id', 'عنوان', "تاریخ رزرو",  "ساعت", 'زمان ثبت', ]

    @staticmethod
    def get_serializer_fields():
        return ['id',
                'title',
                'reserve_date',
                'reserve_time',
                'created_at',
                'description',
                ]
