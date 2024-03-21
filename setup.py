from skbuild import setup

# run setup installation command
setup(name='example',
      version='0.1',
      packages=['example'],
      package_dir={'example':'py/src/example'},
      cmake_install_dir='py/src/example')
