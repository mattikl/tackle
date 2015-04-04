from setuptools import setup, find_packages

setup(
    name='tackle',
    version='0.0.1',
    author='Matti Korttila',
    author_email='matti.korttila@gmail.com',
    url='https://github.com/mattikl/tackle',
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'tablib',
    ],
    entry_points='''
        [console_scripts]
        tackle=tackle:cli
        tackle-mgmt=tackle.mgmt:mgmt
    ''',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Topic :: Utilities',
    ),
)
