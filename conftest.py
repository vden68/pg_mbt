# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
import json
import os.path
from datetime import datetime

from fixture.application import Application
from fixture.db import Dbfixture
from fixture.generator import Generatorfixture


from model.mbt_host import Mbt_hosts
from model.mbt_conn import Mbt_conn


fixture = None
target = None
dbfixture = None
generatorfixture = None


def load_mbt_hosts():
    mbt_hosts = []
    mbt_hosts_p = read_config_file(argument="mbt_hosts")
    for mbt_host in mbt_hosts_p:
        mbt_hosts.append(Mbt_hosts(host=mbt_host["host"], port=mbt_host["port"],
                                   write=mbt_host['write'], read=mbt_host['read']))
    return mbt_hosts

def load_mbt_conn():
    mbt_conn_r = read_config_file(argument="mbt_conn")
    mbt_conn=Mbt_conn(superuser=mbt_conn_r["superuser"], superuser_password=mbt_conn_r["superuser_password"],
                      user=mbt_conn_r['user'], password=mbt_conn_r['password'], database=mbt_conn_r['database'],
                      test_start_timestamp=datetime.now())
    return mbt_conn


def read_config_file(argument=None):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/mbt_hosts.json')
    with open(config_file) as f:
        mbt_hosts_json = json.load(f)
        mbt_hosts_p = mbt_hosts_json[argument]
    return mbt_hosts_p


@pytest.fixture
def app(request):
    global fixture


    if fixture is None :
        mbt_hosts = load_mbt_hosts()
        mbt_hosts_write = [x for x in mbt_hosts if x.write == "True"]
        mbt_hosts_read = [x for x in mbt_hosts if x.read == "True"]

        mbt_conn= load_mbt_conn()

        fixture = Application(mbt_hosts, mbt_hosts_write, mbt_hosts_read, mbt_conn)

    return fixture


@pytest.fixture
def db(request, app):
    global dbfixture

    if dbfixture is None:
        dbfixture = Dbfixture(app)

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)

    return dbfixture


@pytest.fixture
def generator(request):
    global generatorfixture

    if generatorfixture is None:
        generatorfixture = Generatorfixture()

    def fin():
        generatorfixture.destroy()

    request.addfinalizer(fin)

    return generatorfixture
