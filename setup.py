from setuptools import setup

VERSION = '0.1'
PACKAGE = 'htblowfishstore'

setup(
    name = 'HtBlowfishStorePlugin',
    version = VERSION,
    description = "HtPasswdStore for Trac's AccountManager with Blowfish support.",
    author = 'Mitar',
    author_email = 'mitar.trac@tnode.com',
    url = 'http://mitar.tnode.com/',
    keywords = 'trac plugin',
    license = 'GPLv3',
    packages = [PACKAGE],
    include_package_data = True,
    install_requires = [
        'TracAccountManager',
        'bcrypt',
    ],
    zip_safe = False,
    entry_points = {
        'trac.plugins': '%s = %s' % (PACKAGE, PACKAGE),
    },
)
