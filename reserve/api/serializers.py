from badi_utils.dynamic_api import api_error_creator, DynamicSerializer, CustomValidation
from badi_utils.validations import PersianValidations
from rest_framework import serializers

from ..models import *


class ReserveSerializer(DynamicSerializer):
    class Meta:
        model = Reserve
        extra_kwargs = api_error_creator(model, model.get_serializer_fields(),
                                         blank_fields=[],
                                         required_fields=['title'])
        fields = model.get_serializer_fields()

