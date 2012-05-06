#!/usr/bin/env python
# Generated by jaraco.develop (https://bitbucket.org/jaraco/jaraco.develop)
import setuptools

setup_params = dict(
	name='pytest-runner',
	use_hg_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	url="https://bitbucket.org/jaraco/pytest-runner",
	packages=setuptools.find_packages(),
	zip_safe=True,
	entry_points = {
		'distutils.commands':
			['pytest_runner = pytest_runner.command:PyTest'],
	},
	setup_requires=[
		'hgtools',
	],
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
