# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
import json
import os.path

from fixture.application import Application
from fixture.db import Dbfixture


from model.mbt_host import Mbt_hosts

fixture = None
target = None
mbt_hosts = None

def load_mbt_hosts():
    global mbt_hosts
    if mbt_hosts is None:
        mbt_hosts = []
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__))+'/mbt_hosts.json')
        with open(config_file) as f:
            mbt_hosts_json = json.load(f)
            mbt_hosts_p = mbt_hosts_json["mbt_hosts"]
        for mbt_host in mbt_hosts_p:
            mbt_hosts.append(Mbt_hosts(host=mbt_host["host"], superuser=mbt_host["superuser"],
                                       superuser_password=mbt_host["superuser_password"], user=mbt_host["user"],
                                       password=mbt_host["password"], database=mbt_host["database"],
                                       port=mbt_host["port"], write=mbt_host['write'], read=mbt_host['read']))

    return mbt_hosts

@pytest.fixture
def app(request):
    global fixture
    mbt_hosts= load_mbt_hosts()


    if fixture is None :
        fixture = Application(mbt_hosts)



    return fixture

@pytest.fixture
def db(request):
    pass
    """

    dbfixture = Dbfixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture
    """