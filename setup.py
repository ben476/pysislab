from setuptools import setup, find_packages

setup(
   name='pysislab',
   version='0.0.1',
   description='Package to fetch data from the CRISiSLab seismometer network',
   author='Ben Hong',
   packages=find_packages(),
   entry_points={
      'console_scripts': [
         'pysislab=pysislab.cli:main',
      ],
   },
)