from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reputation-visibility-matrix",
    version="1.0.0",
    author="BuildYourReputation.online",
    author_email="info@buildyourreputation.online",
    description="Reputation Visibility Matrix is a digital reputation analysis framework for analyzing brand visibility and reputation signals across the digital landscape.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://buildyourreputation.online",
    project_urls={
        "Homepage": "https://buildyourreputation.online",
        "GitHub": "https://github.com/build-your-reputation-online/reputation-visibility-matrix",
        "Documentation": "https://reputation-visibility-matrix.readthedocs.io",
        "PyPI": "https://pypi.org/project/reputation-visibility-matrix",
    },
    py_modules=["reputation_matrix"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "reputation-visibility-matrix",
        "digital-reputation-analysis",
        "brand-visibility",
        "reputation-audit",
        "online-mentions",
        "branded-search",
        "reputation-scoring",
        "buildyourreputation",
    ],
    entry_points={
        "console_scripts": [
            "reputation-matrix=reputation_matrix:main",
        ],
    },
)
