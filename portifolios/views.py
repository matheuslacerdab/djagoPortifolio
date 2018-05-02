# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def portifolio_exibir(request):
	return render(request, 'portifolios/portifolio_exibir.html', {})
