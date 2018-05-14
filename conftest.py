# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from model.mbt_host import Mbt_hosts
#from fixture.orm import ORMFixture

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
            mbt_hosts.append(Mbt_hosts(host=mbt_host["host"], user=mbt_host["user"], password=mbt_host["password"],
                          database=mbt_host["database"], port=mbt_host["port"], type=mbt_host['type']))

    return mbt_hosts

@pytest.fixture
def app(request):
    global fixture
    mbt_hosts= load_mbt_hosts()


    if fixture is None :
        fixture = Application(mbt_hosts)

    return fixture


"""
@pytest.fixture(scope='session')
def orm(request):
    orm_config = load_config(request.config.getoption("--target"))["db"]
    ormfixture = ORMFixture(host=orm_config["host"], name=orm_config["name"], user=orm_config["user"], password=orm_config["password"])
    return ormfixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")



def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])



def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
"""