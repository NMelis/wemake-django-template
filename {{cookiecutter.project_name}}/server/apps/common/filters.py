# -*- coding: utf-8 -*-

from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _


class _SearchContainsFilter(admin.SimpleListFilter):
    template = 'django_admin_listfilter_input/input_filter.html'

    def expected_parameters(self):
        return []

    def __init__(self, field, request, params, model):
        self.lookup_kwarg = '{0}__contains'.format(self.parameter_name)
        super().__init__(field, request, params, model)

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = dict()
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

    def queryset(self, request, queryset):
        term = self.value()

        if term is None:
            return queryset
        return queryset.filter(**{self.lookup_kwarg: term})


# class AddressContainsFilter(_SearchContainsFilter):
#     """Поля для фильтра 'model_field' по частичному совпадению."""
#
#     parameter_name = 'model_field'
#     title = _('Title name')
