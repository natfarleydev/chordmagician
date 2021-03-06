from setuptools import setup


setup(
    name="chordmagician",
    version="0.3.0b0",
    description="A magical script to create random chords with ABC notation.",
    author="Nathanael Farley",
    author_email="nasfarley88",
    url="https://github.com/natfarleydev/chordmagician",
    packages=["chordmagician"],
    package_data={"chordmagician": ["*.yaml"]},
    scripts=["scripts/chordmagician"],
    install_requries=[],  # All uses standard library
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "astroid==2.4.1",
            "attrs==19.3.0",
            "black==19.10b0",
            "click==7.1.2",
            "hypothesis==5.16.0",
            "isort==4.3.21",
            "lazy-object-proxy==1.4.3",
            "mccabe==0.6.1",
            "more-itertools==8.3.0",
            "packaging==20.4",
            "pathspec==0.8.0",
            "pluggy==0.13.1",
            "py==1.8.1",
            "pylint==2.5.2",
            "pyparsing==2.4.7",
            "pytest==5.4.2",
            "regex==2020.5.14",
            "rope==0.17.0",
            "six==1.15.0",
            "sortedcontainers==2.1.0",
            "toml==0.10.1",
            "typed-ast==1.4.1",
            "wcwidth==0.1.9",
            "wrapt==1.12.1",
        ]
    },
)
