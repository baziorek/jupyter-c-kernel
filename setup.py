from setuptools import setup

setup(name='jupyter_cpp_kernel',
      version='1.2.1',
      description='Minimalistic C++ kernel for Jupyter',
      author='Brendan Rius',
      author_email='ping@brendan-rius.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/baziorek/jupyter-cpp-kernel',
      download_url='https://github.com/baziorek/jupyter-cpp-kernel/tarball/1.2.1',
      packages=['jupyter_cpp_kernel'],
      scripts=['jupyter_cpp_kernel/install_cpp_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'cpp'],
      include_package_data=True
      )
