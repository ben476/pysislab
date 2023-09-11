from setuptools import setup, find_packages

# annotated-types==0.5.0
# certifi==2023.7.22
# charset-normalizer==3.2.0
# idna==3.4
# importlib-metadata==6.8.0
# markdown-it-py==3.0.0
# mdurl==0.1.2
# msgpack==1.0.5
# pydantic==2.3.0
# pydantic_core==2.6.3
# Pygments==2.16.1
# requests==2.31.0
# rich==13.5.2
# typeguard==4.1.5
# typing_extensions==4.7.1
# urllib3==2.0.4
# websocket-client==1.6.3
# zipp==3.16.2

setup(
   name='pysislab',
   description='Package to fetch data from the CRISiSLab seismometer network',
   author='Ben Hong',
   packages=find_packages(),
   entry_points={
      'console_scripts': [
         'pysislab=pysislab.cli:main',
      ],
   },
   install_requires=[
      'rich',
      'requests',
      'websocket-client',
      'msgpack',
      'pydantic',
      'typeguard',
   ],
)