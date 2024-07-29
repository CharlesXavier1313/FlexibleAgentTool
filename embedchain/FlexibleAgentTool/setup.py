from setuptools import setup, find_packages
setup(
    name="FlexibleAgentTool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'numpy',
        'pandas',
        'scikit-learn'
    ],
)
