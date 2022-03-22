from setuptools import setup 

setup (             #méthode setup qui permettra l’installation de la librairie sur le système
    name='lib_projet' , 
    version = '1.0' ,
    author= 'Groupe',
    author_email= 'zackboum.zb@gmail.com',
    description = " Cette libraire en Python permet d'automatiser la parallélisation maximale de systèmes de tâches"
    licence = ''
    keywords = ''
    url = ''
    packages=[                          #Packages de la librairie
              'lib_projet'
              ], 
    long_description=open('README.md').read(),      #Fichier README contenant le role de la librairie
    classifiers=[
            ' Development statut :: 4 - Beta' ,
            'Intended Audience :: Developers' ,
            'License :: Proprietary Llicense',
            'Natural Language :: French',
            'Operating System :: OS Iindependent',
            'Operating System :: Python :: 3.7' ,
            'Topic :: Software Development' , 
            'Topic :: Software Development :: Libraries :: Python Modules' , 
            "Topic :: Utilities"
    ]
    install_requires=[
        'pymongo==3.7.2'
    ],
    include_package_data=True
    )