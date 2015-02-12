from setuptools import setup

setup(
    name='tackle',
    version='0.0.1',
    packages=['tackle'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        tackle=tackle:cli
    ''',
)
