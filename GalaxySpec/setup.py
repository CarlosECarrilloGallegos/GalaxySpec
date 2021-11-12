import setuptools

setuptools.setup(
    name="galaxyspec",
    version="0.1",
    author="Carlos Carrillo-Gallegos",
    author_email="carlos.carrillo-gallegos@yale.edu",
    description="Galactic Spectral Extraction and Fitting Package",
    packages=["galaxyspec", "galaxyspec/fitting"],
    install_requires=["numpy","scipy"]
)
