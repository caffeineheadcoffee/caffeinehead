from django.views import generic
from ..forms import EnquiryForm

from apps.order.mixins import OrderMixin
from apps.website import forms

from apps.website.models import *
from apps.website.forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class AboutUsView(OrderMixin, generic.TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context


class ServicesView(OrderMixin, generic.TemplateView):
    template_name = 'pages/services/index.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context.update({
                'order_items_count': self.get_order_items_count(),
            })
        return context


class ContractRoastingServiceView(ServicesView):
    template_name = 'pages/services/contract_roasting.html'


class AppDevelopmentServiceView(ServicesView):
    template_name = 'pages/services/app_development.html'


class CoffeeCocktailsServiceView(ServicesView):
    template_name = 'pages/services/coffee_cocktails.html'


class CyberSecurityServiceView(ServicesView):
    template_name = 'pages/services/cyber_security.html'


class MspServiceView(ServicesView):
    template_name = 'pages/services/msp.html'


class PosServiceView(ServicesView):
    template_name = 'pages/services/pos.html'


class WholesaleServiceView(ServicesView):
    template_name = 'pages/services/wholesale.html'


class ContactUsView(OrderMixin, generic.FormView):
    template_name = 'pages/contact_us.html'
    form_class = EnquiryForm

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context.update({
            'order_items_count': self.get_order_items_count(),
        })
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PartnershipView(ServicesView):
    template_name = 'pages/partnership.html'

def index(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form submitted !!")
            return redirect('/form')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify form !!')
            return render(request,'pages/partnership.html',{
                'form':form
            })
    context = {
        'form':SubmissionForm()
    }
    return render(request, 'pages/partnership.html', context)

@login_required
def services(request):
    services = Submission.objects.all()
    context = {
        'services': services
    }
    return render(request, 'pages/showservices.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for contacting us.")
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify form !!')
            return render(request,'pages/partnership.html',{
                'form':form
            })
    context = {
        'form':ContactForm()
    }
    return render(request, 'pages/partnership.html', context)

@login_required
def show_message(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'pages/messages.html', context)

# @login_required
# def partnership(request):
#     if request.method == 'POST':
#         submission_form = SubmissionForm(request.POST, prefix='serviceform')
#         contact_form = ContactForm(request.POST, prefix='contact')

#         if submission_form.is_valid():
#             index()
#         elif contact_form.is_valid():
#             contact()
#         else:
#             messages.error(request, 'Please verify the forms.')

#     return render(request, 'pages/partnership.html', {
#         'submission_form': SubmissionForm(prefix='serviceform'),
#         'contact_form': ContactForm(prefix='contact'),
#     })
