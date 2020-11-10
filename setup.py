from setuptools import setup , find_packages

requirements = {
"aniso8601==8.0.0",
"click==7.1.2",

#flask specific
"Flask==1.1.2",
"Flask-Cors==3.0.9",
"Flask-RESTful==0.3.8",
#standart modules
"Jinja2==2.11.2",
"MarkupSafe==1.1.1",
"pytz==2020.4",
"six==1.15.0",
"Werkzeug==1.0.1"
}

setup(
    neme="Artify",
    description="Artify - download API service",
    version="0.0.1",
    packages= find_packages(),
    install_requires=requirements,

    classifiers=(
        "Deployment Status :: 0 ",
        "framework :: flask",
        "Programing Language :: Python 3"
    ),
    platform="python 3.8.6 and later"

)