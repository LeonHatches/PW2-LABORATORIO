from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .renders import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "Leon Hatches",
            "amount": 1399.00,
            "today": "today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("prueba")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            
            response['Content-Disposition'] = content
            return response
        
        return HttpResponse("Not Found")