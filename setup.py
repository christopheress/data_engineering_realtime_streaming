from setuptools import setup, find_packages
import schema

requires = [
    "dataclasses-avroschema",
    "faust-streaming",
    "python-schema-registry-client",
    "simple-settings"
]

setup(
    name='faust-example',
    version='1.2.2',
    description='Faust example with Docker Compose',
    classifiers=[
        "Programming Language :: Python"
    ],
    author='Christopher Essmann',
    author_email='christopher.essmann@web.de',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'faust.codecs': [
            'avro_traffic = schema:avro_traffic_codec',
            'avro_weather = schema:avro_weather_codec'
        ]
    }
)
