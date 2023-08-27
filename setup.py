from setuptools import setup

setup(
    name='bf5py_custom',
    version='0.1.0',    
    description='Fork for bf4py',
    url='https://github.com/MoSafi2/bf4py',
    author='Not me',
    author_email='',
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['urllib,
                    hashlib,
                    requests,
                    json,
                    sseclient
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
    ],
)
