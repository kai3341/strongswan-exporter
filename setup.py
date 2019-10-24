import os
import pathlib
from setuptools import setup

# Костыль года: скрипт запускается несколько раз из разных директорий
if 'PROJECT_ROOT' in os.environ:
    CWD = os.environ['PROJECT_ROOT']
else:
    CWD = os.path.abspath(__file__)
    CWD = os.path.dirname(CWD)
    os.environ['PROJECT_ROOT'] = CWD

CWD = pathlib.Path(CWD)


README = CWD / 'README.md'
HISTORY = CWD / 'HISTORY.md'

with README.open() as readme_file:
    readme = readme_file.read()

with HISTORY.open() as history_file:
    history = history_file.read()

classifiers = (
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
)

requirements = (
    'vici',
)

long_description = '\n\n'.join((readme, history))

keywords = (
    'strongswan',
    'prometheus',
    'monitoring',
)

scripts = (
    'exporter.py',
)

setup(
    classifiers=classifiers,
    description="Strongswan monitoring metric exporter",
    install_requires=requirements,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords=keywords,
    name='strongswan-exporter',
    scripts=scripts,
    url='https://github.com/kai3341/strongswan-exporter',
    version='0.0.1',
    zip_safe=True,
)
