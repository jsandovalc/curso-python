from django.views.generic.edit import CreateView
from .models import Bill
from .forms import ItemFormSet
from django.urls import reverse_lazy
from django.db import transaction


class BillItemCreate(CreateView):
    model = Bill

    fields = ['nit', 'bill_type']
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['items'] = ItemFormSet(self.request.POST)
        else:
            data['items'] = ItemFormSet()
        return data

    def form_valid(self, form):
        print(1)
        context = self.get_context_data()
        print(2, context)
        items = context['items']
        print(3, items)
        with transaction.atomic():
            print(4)
            self.object = form.save()

            if items.is_valid():
                print(5)
                items.instance = self.object
                items.save()

        return super().form_valid(form)
