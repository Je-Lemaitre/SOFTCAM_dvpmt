from setuptools import setup, find_packages

setup(
    name='SOFTCAM',
    version='1',
    description='This software aims to help engineers in cam design',
    author='Jérémy LEMAITRE',
    author_email='jeremy.lemaitre@ensta-bretagne.org',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
    ],
    extras_require={
        'extra_feature': ['dependency3', 'dependency4']
    }
)