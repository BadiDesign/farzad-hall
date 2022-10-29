from badi_utils.dynamic_api import DynamicModelApi
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from reserve.api.serializers import *
from reserve.filter import *
from reserve.models import *


class ReserveViewSet(DynamicModelApi):
    model = Reserve
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [permissions.AllowAny]
    custom_perms = {
    }
    filterset_class = ReserveFilter

    @action(methods=['get'], detail=False)
    def calendar(self, request, *args, **kwargs):
        data = []
        for reserve in self.model.objects.all():
            data.append({
                "id": reserve.id,
                "className": "fc-event-solid-primary",
                "title": reserve.title,
                "start": reserve.reserve_date.isoformat(),
            })
        return Response(data)

    def filter_queryset(self, qs):
        if self.action == 'datatable':
            return self.filterset_class(self.request.data).qs
        return super().filter_queryset(qs)


class CustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'limit'
    max_page_size = 9
