from setuptools import setup

setup(
    name='chessQuest',
    version='1.0.0',
    packages=['chessQuest'],
    url='https://github.com/RedXBeard/chessQuest',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    author='Barbaros Yildirim',
    author_email='barbarosaliyildirim@gmail.com',
    description='',
    include_package_data=True,
    entry_points={
        'console_scripts': ['chessquest=chessQuest.command:main'],
    },
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7 :: 3',
    ],
)
