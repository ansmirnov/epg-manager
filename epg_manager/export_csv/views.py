from django.shortcuts import render_to_response
from epg_core.models import *

def export_csv(request):
    return render_to_response('export_csv.csv', {
        'programmes': Programme.objects.all(),
    })