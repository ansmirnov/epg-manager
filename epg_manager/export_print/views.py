from django.shortcuts import render_to_response
from epg_core.models import *
import datetime


def export_print(request):
    _date = request.GET.get('date', '')
    if _date == '':
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(_date, "%d.%m.%Y").date()
    return render_to_response('export_print.html', {
        'channels': Channel.objects.all(),
        'date': date,
    })
