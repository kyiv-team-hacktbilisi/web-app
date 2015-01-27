from setuptools import setup, find_packages
import sys

install_requires = ['redis', 'motor', 'jinja2', 'yuicompressor', 'webassets',
                    'cssmin', 'PyYAML']
# 'Routes'

if sys.version_info == (3,3):           # Python 3.4 introduced `asyncio` in standard library,
    install_requires.append('asyncio')  # it was backported for 3.3 as a pypi module

setup(name='scheduler',
      version='0.1',
      author='Sviatoslav Sydorenko',
      author_email='wk@sydorenko.org.ua',
      package_dir={'': 'src'},
      packages=find_packages('src', exclude=["test**"]),
      install_requires=install_requires,
      zip_safe=False)
