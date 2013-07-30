from distutils.core import setup

setup(
    name='OT',
    version='0.1.0',
    author='Alex Djalali',
    author_email='alex.djalali@gmail.com',
    packages=['ot', 'ot.test'],
    url='https://github.com/alexdjalali/OT',
    description='Rank optimality theory constraints, entailments, etc.',
    long_description=open('README').read()
)
