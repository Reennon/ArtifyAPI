from setuptools import setup , find_packages

requirements = {

#flask specific
"Flask==1.1.2",
"Flask-Cors==3.0.9",
"Flask-RESTful==0.3.8",


}

setup(
    name="Artify",
    description="Artify - download API service",
    version="0.0.1",
    packages= find_packages(),
    install_require=requirements,
    extras_require={
        "dev":requirements
    },

    classifiers=[
        "Development Status :: 0 - init",
        "framework :: Flask",
        "Programming Language :: Python :: 3"
    ],
    platform="python 3.8.6 and later."

)