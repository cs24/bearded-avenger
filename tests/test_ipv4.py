import pytest

from cif.observable import Observable


def _not(data):
    for d in data:
        d = Observable(d)
        assert d.otype is not 'ipv4'


def test_ipv4_ipv6():
    data = ['2001:1608:10:147::21', '2001:4860:4860::8888']
    _not(data)


def test_ipv4_fqdn():
    data = ['example.org', '1.2.3.4.com', 'xn----jtbbmekqknepg3a.xn--p1ai']
    _not(data)


def test_ipv4_urls():
    data = [
        'http://192.168.1.1/1.html',
        'http://www41.xzmnt.com',
        'http://get.ahoybest.com/n/3.6.16/12205897/microsoft lync server 2010.exe'
    ]
    _not(data)


def test_ipv4_ok():
    data = ['192.168.1.0/24', '192.168.1.1', '255.255.255.255']
    for d in data:
        assert Observable(observable=d).otype is 'ipv4'


def test_ipv4_private():
    data = ['128.205.1.0/24', '2001:1608:10:147::21', '2001:4860::8888/64']
    for d in data:
        assert not Observable(observable=d).is_private()

    assert Observable('192.168.1.1').is_private()