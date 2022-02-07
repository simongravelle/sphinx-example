from setuptools import setup

setup(name='python-sample-project',
      version='v0.1.0',
      description='Python sample project to illustrate the use of sphinx documentation',
      long_description=open('README.rst').read(),
      long_description_content_type='text/x-rst',
      url='https://github.com/simongravelle/python-sample-project',
      author='Simon Gravelle',
      author_email='simon.gravelle@live.fr',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=['myproject'],
      zip_safe=False
      )
