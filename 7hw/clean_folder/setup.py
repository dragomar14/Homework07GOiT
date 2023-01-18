from setuptools import setup, find_namespace_packages

setup(
    name='cleanup-dmytro_m',
    version='0.0.1',
    description='cleanup script which built with python-packages and console script.',
    url='https://github.com/dragomar14/Homework07GOiT',
    author='Dmytro Marchenko',
    author_email='dragomar14@gmail.com',
    license='MIT',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    install_requires=['shutil', 'pathlib', 'os', 're', 'sys'],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
        ]
    }
)