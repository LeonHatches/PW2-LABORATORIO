from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
from .renders import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pdf/index.html', {})
    
    def post(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        
        file  = request.POST.get('filename')
        title = request.POST.get('title')
        text  = request.POST.get('text')
        download = request.POST.get('download')
        
        context = {
            "title": title,
            "text": text,
        }

        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = '%s.pdf' %(file)
            content = "inline; filename=%s" %(filename)

            if download:
                content = "attachment; filename=%s" %(filename)
            
            response['Content-Disposition'] = content
            return response
        
        return HttpResponse("Not Found")