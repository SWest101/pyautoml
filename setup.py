from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pyautoml',
    version='0.1',
    description='Python wrapper for the Featuretools and TPOT packages',
    long_description=readme(),
    url='http://github.com/SWest101/pyautoml',
    author='Shaun van der Westhuizen',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=open('requirements.txt').readlines(),
    test_suite='nose.collector',
    tests_require=['nose'],
    python_requires='>=3.5',
    keywords='feature engineering data science machine learning TPOT Featuretools'
)