from setuptools import setup

version = "0.1"

setup(
    name="yamltools",
    version=version,
    description="tools for dealing with YAML from command line",
    author="Andrey Popp",
    author_email="8mayday@gmail.com",
    py_modules=["yamltools"],
    test_suite="tests",
    zip_safe=False,
    entry_points="""
    [console_scripts]
    yaml = yamltools:main
    """)
