# Whisper

## Setup
Use Python 3.9.9 and PyTorch 1.10.1


Download and install
```shell
pip install -U openai-whisper
```

Alternatively, the following command will pull and install the latest commit from this repository
```shell
pip install git+https://github.com/openai/whisper.git
```

Requires the command-line tool ffmpeg to be installed on your system
```shell
# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg
```

You may need rust installed.
```shell
pip install setuptools-rust
```

## Command-line usage
```shell
whisper Flotsam.mp3
```

## Execute python script
```shell
pyhton Whisper.py
```
