from badi_utils.dynamic import DynamicCreateView, DynamicUpdateView

from reserve.filter import ReserveFilter
from reserve.models import Reserve


class ReserveCreateView(DynamicCreateView):
    model = Reserve
    extra_context = {
        'filter_form': ReserveFilter().form
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ReserveUpdateView(DynamicUpdateView):
    model = Reserve

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ReserveDetailView(DynamicUpdateView):
    model = Reserve
    template_name = 'reserve/reserve_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
