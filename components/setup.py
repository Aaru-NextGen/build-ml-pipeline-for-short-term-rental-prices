from setuptools import setup


setup(
    name="wandbutils",
    version=0.1,
    description="Utilities for interacting with Weights and Biases and mlflow",
    zip_safe=False,  # avoid eggs, which make the handling of package data cumbersome
    packages=["wandbutils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
    ],
    install_requires=[
        "mlflow",
        "wandb"
    ]
)
