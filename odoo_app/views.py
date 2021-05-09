from django.shortcuts import render
from xmlrpc import client
from rest_framework.decorators import api_view
from rest_framework.response import Response

db = 'newtest'
url = 'http://localhost:8069'
# import pdb;pdb.set_trace()
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))

def get_uid():
    username = 'admin'
    password = 'admin'
    uid = common.authenticate(db, username, password, {})
    return uid, password

def execute(*args, rest):
    if 'uid' not in rest.session:
        uid = get_uid()[0]
        rest.session['uid'] = uid
        rest.session['password'] = get_uid()[1]
    uid = rest.session['uid']
    password = rest.session['password']
    return models.execute_kw(db, uid, password, *args)

@api_view(['GET'])
def get_contacts_list(request):
    contacts = execute('res.partner', 'search_read', [[]], {'fields':['name']}, rest=request)
    return Response({'result': contacts, 'status_code': 200})

@api_view(['GET'])
def get_contact(request, pk):
    contacts = execute('res.partner', 'search_read', [[['id','=',pk]]], {'fields':['name']}, rest=request)
    return Response({'result': contacts, 'status_code': 200})
