from distutils.core import setup

setup(
    name='ot',
    version='0.5.0',
    author='Alex Djalali',
    author_email='alex.djalali@gmail.com',
    packages=['ot', 'ot.test'],
    url='https://github.com/alexdjalali/OT',
    description='Rank optimality theory constraints, entailments, etc.',
    long_description=open('README.rst').read(),
    install_requires=[
        'pymongo==2.5.2'
    ]
)
