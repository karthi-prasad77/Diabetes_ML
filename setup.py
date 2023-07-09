from setuptools import setup

setup(
    name="src",
    version=0.1,
    description="Diabetes prediction using navie bayes algorithm",
    author="Karthi Prasad",
    author_email="karthiprasad44@gmail.com",
    packages=['src'],
    install_requires = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit_learn",
        "streamlit",
        "notebook",
        "tqdm",
        "setuptools",
    ]
)