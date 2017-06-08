from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

def read(relpath):
	with open(path.join(here, *relpath.split('/')), encoding='utf-8') as f:
		return f.read().strip()

setup(
	name='template',
	version=read('VERSION'),
	description='template',
	long_description=read('README.md'),
	url='https://github.com/timbertson/template',
	py_modules=["template"],
	install_requires=["jinja2"],
	scripts = ['template'],
)

