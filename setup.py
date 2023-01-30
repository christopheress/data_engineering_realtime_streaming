from setuptools import setup, find_packages

requires = [
    "colorlog>=3.1.4",
    "dataclasses-avroschema",
    "faust",
    "python-schema-registry-client",
    "yarl<1.6.0,>=1.0",
    "multidict<5.0,>=4.5",
    "simple-settings",
    "typing-extensions",
]

setup(
    name='faust-example',
    version='1.2.2',
    description='Faust example with Docker Compose',
    long_description='''
    Example running Faust with Docker Compose (zookeeper, kafka and schema-registry)
    ''',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Christopher Eßmann',
    author_email='christopher.essmann@web.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        'faust.codecs': [
            'avro_traffic = producer.schema:avro_traffic_codec',
        ],
    },
)