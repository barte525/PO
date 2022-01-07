from django.views import View
from django.shortcuts import render
from mysite.models.segment import CustomSegment, DefinedSegment, Segment

class ViewSegments(View):
    def get(self, request):
        definedSegments = list(DefinedSegment.objects.all())
        customSegments = list(CustomSegment.objects.all())
        return render(request, 'viewsegments.html', {'definedSegments': definedSegments, 'customSegments': customSegments})
