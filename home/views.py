from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from home.models import Customer, Next_of_kin


def home(request):
    context = {}
    return render(request, 'home/home.html', context)


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'home/customer/customer_create.html'
    fields = '__all__'


class CustomerListView(ListView):
    model = Customer
    template_name = 'home/customer/customer_list.html'
    context_object_name = 'customers'
    ordering = ['-dated_registered']
    # paginate_by = 5


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'home/customer/customer_detail.html'

    def get_queryset(self):
        customer = Customer.objects.all()
        # next_of_kin = Next_of_kin.objects.all()
        return customer
