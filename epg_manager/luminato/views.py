from django.shortcuts import render_to_response
from luminato.models import LuminatoChannel


def config(request):
    return render_to_response("config.cfg", {
        'channels': LuminatoChannel.objects.all()
    })