from setuptools import setup
import io

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='pydftd3',
  packages=['pydftd3'],
  version='1.0',
  description='Python version of Grimme\'s D3-dispersion correction for Gaussian input/output',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Paton Research Group',
  author_email='robert.paton@colostate.edu',
  url='https://github.com/patonlab/pyDFTD3',
  download_url='https://github.com/patonlab/pyDFTD3/archive/v1.0.zip',
  keywords=['gaussian', 'dispersion-energies', 'dampening-parameters', 'becke-johnson', 'grimme'],
  classifiers=[],
  install_requires=["cclib"],
  python_requires='>=2.6',
  include_package_data=True,
)

