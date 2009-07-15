from datetime import date
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import conditional_escape as esc
from django.utils.safestring import mark_safe

from promos.forms import *
from promos.models import *

def promo_billboard_homepage(request):
    """
    Get promo details.
    """
    today = date.today()
    billboards = PromoBillboard.objects.filter(start_date=date.today())
    
    return render_to_response(
            'promo_billboard_homepage.html',{
            'billboards': billboards,

             },
              context_instance=RequestContext(request))