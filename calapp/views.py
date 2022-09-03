from audioop import add
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from calapp.forms import spend_form
from .models import add_spends
from django.urls import reverse
from django.db.models import Sum
# Create your views here.
class template_view(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        if 'date' in kwargs:
            context = super().get_context_data(**kwargs)
            print(kwargs)
            context["data"] = add_spends.objects.filter(date__date=kwargs['date'])
            print(context)
            context['group']=add_spends.objects.filter(date__date=kwargs['date']).values('date__date').annotate(dtotal=Sum('amount')).order_by('-date__date')
        else:
            context = super().get_context_data(**kwargs)
            context["data"] = add_spends.objects.all()
            context['group']=add_spends.objects.values('date__date').annotate(dtotal=Sum('amount')).order_by('-date__date')
            print(context)
            # print(kwargs)
        return context
    
    def get_queryset(self):
        print(self.kwargs)
        return super().get_queryset()
    
    
    
class add_view(CreateView):
    model=add_spends
    # fields=['reason','amount','type']
    template_name='add.html'
    success_url='ho'
    form_class=spend_form
    