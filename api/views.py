import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from core.models import Lead


def connect(request: WSGIRequest):
    lead = Lead(
        name='oli',
        email='test@test.com',
        message='holaaaa'
    )
    # leads = Lead.objects.all()
    leads = list()
    lead_dict = {
        'id': 1,
        'name': 'oli',
        'email': 'test@test.com',
        'message': 'holaaaa'
    }

    leads.append(lead_dict)
    leads.append(lead_dict)

    leads_json = json.dumps(leads)

    return HttpResponse(f"{leads_json}")
