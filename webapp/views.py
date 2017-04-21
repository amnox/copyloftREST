# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def landing(request):
	template = loader.get_template('index.html')
	context = {
		'data': 200,
	}
	return HttpResponse(template.render(context, request))