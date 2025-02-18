from setuptools import setup, find_packages

setup(
    name="notebookcellui",
    version="0.1.0",
    description="A JupyterLab extension with both frontend and backend",
    author="labcomputer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jupyterlab>=4.0.0',
        "jupyter_server",
        'flask',
        'watchmedo',
    ],
    zip_safe=False,
    entry_points={
        'jupyter_serverproxy_servers': [
            'notebookcellui = notebookcellui:load_jupyter_server_extension',
        ]
    },
    # Entry points for the Jupyter Server Extension
    data_files=[
        ("share/jupyter/labextensions/notebookcellui", [
            "static/labextension/static/*"
        ]),
        ('etc/jupyter/jupyter_server_config.d', [
            'notebookcellui/jupyter_server_config.json'
        ])
    ],
    classifiers=[
        "Framework :: Jupyter",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

# __import__('setuptools').setup()
