from setuptools import setup, find_packages

setup(
    name='HeatMapPatternOfLife',  # Package name
    version='0.1',  # Version number
    author='Colin Cowie',  # Your name
    author_email='colin.cowie10@gmail.com',  # Your email
    description='Generate heatmaps to analyze pattern of life from different data formats.',  # Short description
    long_description=open('README.md').read(),  # Long description read from the README.md
    long_description_content_type='text/markdown',  # Type of the long description
    url='https://github.com/colincowie/',  # Link to your GitHub repository or website
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        'pandas',
        'plotly'
    ],  # List of dependencies
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    license='MIT',
)
