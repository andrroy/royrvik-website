from django.shortcuts import render_to_response
from fabric.api import run, local, hosts, cd
from django.template import RequestContext
from vb.models import Server, Operatingsystem, Nat_rules

# def host_type():
#     m = local('vboxmanage list vms', capture=True)
#     return m

import re
def vhost_list():
	input = local('vboxmanage list vms', capture=True)
	vbox_list = re.findall('"([^"]*)"', input)
	return vbox_list

def list_running_vms():
	input = local('VBoxManage list runningvms', capture=True)
	vbox_list = re.findall('"([^"]*)"', input)
	return vbox_list

def home(request):
	vbox_list = vhost_list()
	active_list = list_running_vms()
	
	for server in vbox_list:
		if server in active_list:
			vbox_list.remove(server)

	return render_to_response('vb_home.html', {'active_servers':active_list,'other_servers':vbox_list}, context_instance=RequestContext(request))


def box_details(request, box_name):
	info = local('vboxmanage showvminfo '+box_name, capture=True)

	return render_to_response('box_details.html', {'info':info}, context_instance=RequestContext(request))