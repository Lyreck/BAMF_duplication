# Reverse engineering of name transliteration and matching in immigration databases

This code is linked to our paper on the German and UK's management of immigration databases. We analyzed their use of name transliteration and duplicate detection through a legal, societal and technical lens. 
This code is the technical reverse-engineerering part. It is used in this webpage: [project prototype](https://leo.le.douar.ec/sections/graph_viz.html).

## Installation
You can reproduce this project on your local machine by using uv for most of the packages - except ICU transliteration.

1. Clone the repository to ~/filename
2. move to ~/filename and synchronize the dependencies specified in pyproject.toml: `uv sync`
3. install ICU and PyICU (/!\ It is not included in pyproject.toml since installation of ICU is a bit complex: see next section)

To run the LLM transliteration, you need at least a 15Gb GPU since Mistral-small3.2 weighs 15Gb.

## Installing ICU

### Mac OS with Homebrew

This is the easiest way we found to install ICU and then PyICU with uv. It is not perfect since pyproject.toml is not updated when installing, which means PyICU gets uninstalled at each `uv sync` or `uv remove XX`.
1. install ICU: `brew install icu4c`
2. install PyICU in your local uv environment:
```bash
# For compilers to find icu4c@77 you may need to set:
#  export LDFLAGS="-L/usr/local/opt/icu4c@77/lib"
#  export CPPFLAGS="-I/usr/local/opt/icu4c@77/include"

# For pkgconf to find icu4c@77 you may need to set:
#   export PKG_CONFIG_PATH="/usr/local/opt/icu4c@77/lib/pkgconfig"

# export CC="$(which gcc)" CXX="$(which g++)" (when installing ICU with homebrew)

# uv pip install --no-binary=:all: pyicu
```

### Other methods
To install on other platforms with other methods, please refer to:
- the official [ICU documentation](https://unicode-org.github.io/icu/userguide/)
- the official [PyICU documentation](https://pypi.org/project/pyicu/)
- this guide we found useful: [PyICU cheat sheet](https://gist.github.com/dpk/8325992)


Feel free to reach out if you have any questions or remarks!


