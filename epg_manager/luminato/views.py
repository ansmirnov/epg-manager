from django.shortcuts import render_to_response
from luminato.models import LuminatoChannel


def config(request):
    return render_to_response("config.cfg", {
        'channels': LuminatoChannel.objects.all()
    })


def config_stream(request, stream_id):
    stream_id = int(stream_id)
    return render_to_response("config.cfg", {
        'channels': LuminatoChannel.objects.filter(channel__stream_id=stream_id)
    })
