# -*- coding: utf-8 -*-
__author__ = 'vden'
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from model.mbt_host import Mbt_host
#from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    #browser = request.config.getoption("--browser")
    mbt_config = load_config(request.config.getoption("--target"))["mbt_db_main"]
    main_host= Mbt_host(host=mbt_config["host"], user=mbt_config["user"], password=mbt_config["password"],
                        database=mbt_config["database"], port=mbt_config["port"])
    if fixture is None :
        fixture = Application(main_host)
    #fixture.session.ensure_login(username=mbt_config["username"], password=mbt_config["password"])
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