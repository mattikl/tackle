from setuptools import setup, find_packages

setup(
    name='tackle',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    extras_require={'with_tablib': 'tablib'},
    entry_points='''
        [console_scripts]
        tackle=tackle:cli
        tackle-create=tackle.create:create
    ''',
)
