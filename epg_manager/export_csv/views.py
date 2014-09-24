from django.shortcuts import render_to_response
from epg_core.models import *


def export_csv(request):
    return render_to_response('export_csv.csv', {
        'programmes': Programme.objects.all().order_by('start'),
    })


def export_csv_stream(request, stream_id):
    stream_id = int(stream_id)
    return render_to_response('export_csv.csv', {
        'programmes': Programme.objects.filter(channel__stream_id=stream_id).order_by('start'),
    })
