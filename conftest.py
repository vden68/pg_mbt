# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
import json
import os.path
import uuid
from datetime import datetime
from distutils.util import strtobool

from fixture.application import Application
from fixture.db import Dbfixture
from fixture.generator import Generatorfixture
from fixture.mbtfixture import Mbtfixture


from model.mbt_host import Mbt_hosts
from model.mbt_conn import Mbt_conn


fixture = None
target = None
dbfixture = None
generatorfixture = None
mbtfixture = None


def load_mbt_hosts():
    mbt_hosts = []
    mbt_hosts_p = read_config_file(argument="mbt_hosts")
    for mbt_host in mbt_hosts_p:
        m_test_uuid = str(uuid.uuid1())[0:8]
        mbt_hosts.append(Mbt_hosts(host=mbt_host["host"], node_id=int(mbt_host["node_id"]), port=mbt_host["port"],
                                   write=strtobool(mbt_host['write']), read=strtobool(mbt_host['read'])))
    return mbt_hosts

def load_mbt_conn():
    mbt_conn_r = read_config_file(argument="mbt_conn")
    test_uuid = str(uuid.uuid1())[0:8]
    mbt_conn=Mbt_conn(superuser=mbt_conn_r["superuser"], superuser_password=mbt_conn_r["superuser_password"],
                      user=mbt_conn_r['user'], password=mbt_conn_r['password'], database=mbt_conn_r['database'],
                      test_start_timestamp=datetime.now(), test_uuid=test_uuid,
                      cycle_factor=int(mbt_conn_r['cycle_factor']))
    return mbt_conn


def read_config_file(argument=None):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/mbt_hosts.json')
    with open(config_file) as f:
        mbt_hosts_json = json.load(f)
        mbt_hosts_p = mbt_hosts_json[argument]
    return mbt_hosts_p


@pytest.fixture(scope="session")
def app(request):
    global fixture


    if fixture is None :
        mbt_hosts = load_mbt_hosts()
        mbt_hosts_write = [x for x in mbt_hosts if x.write ]
        mbt_hosts_read = [x for x in mbt_hosts if x.read ]

        mbt_conn= load_mbt_conn()

        fixture = Application(mbt_hosts, mbt_hosts_write, mbt_hosts_read, mbt_conn)

    return fixture


@pytest.fixture(scope="session")
def db(request, app):
    global dbfixture

    if dbfixture is None:
        dbfixture = Dbfixture(app)

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)

    return dbfixture


@pytest.fixture(scope="session")
def generator(request):
    global generatorfixture

    if generatorfixture is None:
        generatorfixture = Generatorfixture()

    def fin():
        generatorfixture.destroy()

    request.addfinalizer(fin)

    return generatorfixture

@pytest.fixture(scope="session")
def mbt(request):
    global mbtfixture

    if mbtfixture is None:
        mbtfixture = Mbtfixture()

    def fin():
        mbt.destroy()

    request.addfinalizer(fin)

    return mbtfixture

