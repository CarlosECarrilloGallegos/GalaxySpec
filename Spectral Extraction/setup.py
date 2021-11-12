import setuptools

setuptools.setup(
    name="spectralfit",
    version="0.1",
    author="Carlos Carrillo-Gallegos",
    author_email="carlos.carrillo-gallegos@yale.edu",
    description="Spectral Extraction and Fitting Package",
    packages=["spectralfit", "spectralfit/fitting"],
    install_requires=["numpy","scipy"]
)
