import json
import time
import requests
from uuid import getnode as get_mac

from hereiam.settings import GOOGLE_MAPS_API

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View

# Create your views here.

class LocationView(View):

	maps_key = GOOGLE_MAPS_API
	base_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
	template = 'location.html'
	try:
		mac = get_mac()
		print("The 48-bit string form of MAC address is %d"% mac)

	except:
		print("NO mac address found!")
		
	def post(self, request):

		try:
			mac = ':'.join(("%012X" % self.mac)[i:i+2] for i in range(0, 12, 2))
			print mac
			data = {
				"wifiAccessPoints" : [
					{
						"macAddress": mac,		
					}
				]}
			headers = {}
			url = self.base_url + self.maps_key
			req = requests.post(url, data=json.dumps(data), headers=headers)
			print req.status_code
			location = req.json()
			return render(request, self.template, {'location': location, 'api': self.maps_key})

		except TypeError:
			print "Use the correct datatype"