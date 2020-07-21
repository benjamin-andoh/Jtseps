from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from home.models import Customer


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
    # ordering = ['-dated_created']
    # paginate_by = 5

