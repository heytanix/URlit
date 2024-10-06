# Text-to-Speech Converter using Google TTS (gTTS)

This Python script converts text input (either manually entered or from a text file) into an audio file using the Google Text-to-Speech (gTTS) library. The output is saved as an MP3 file, which can be played or shared easily.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [1. Convert Text Input to Speech](#1-convert-text-input-to-speech)
  - [2. Convert Text from File to Speech](#2-convert-text-from-file-to-speech)
- [Sample Output](#sample-output)
- [License](#license)

## Overview

This project provides a simple solution to convert any text into an audio file. You can either enter text manually or upload a text file, and the script will generate an MP3 file with the spoken version of the input.

## Features

- Convert manually entered text to an MP3 file.
- Convert text from a file to an MP3 file.
- Support for multiple languages (default is English, but can be adjusted in the code).
- Error handling for text reading and file operations.

## Requirements

To run this script, you will need the following Python packages:

```bash
pip install gtts
