import json
import uuid

from asgiref.sync import sync_to_async
from core.models import Lead
from django.core.handlers.asgi import ASGIRequest
from django.http import HttpResponse


@sync_to_async
def create_lead():
    lead = Lead(name=f"{uuid.uuid4().hex}", email="test@test.com", message="holaaaa")
    lead.save()


# @sync_to_async
# def get_all_leads():
#     return list(Lead.objects.iterator())


async def get_all_leads():
    return await sync_to_async(list)(Lead.objects.iterator())


async def connect(request: ASGIRequest):
    print(f"{request}")
    leads_iterator = await create_lead()
    # leads_iterator = await sync_to_async(list)(Lead.objects.iterator())
    leads = list()
    for lead in await get_all_leads():
        leads.append(
            {
                "id": lead.pk,
                "name": lead.name,
                "email": lead.email,
                "message": lead.message,
            }
        )

    leads_json = json.dumps(leads)
    return HttpResponse(f"{leads_json}")
