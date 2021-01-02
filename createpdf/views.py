from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from cryspy_homepage import utils


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            #  'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = utils.render_to_pdf('pdf_form.html', data)
        return HttpResponse(pdf, content_type='pdf_form')
