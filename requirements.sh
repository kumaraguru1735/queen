#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
  echo "run as root"
  exit 1
fi
sudo apt-get update 
sudo apt-get install -y flac python3 python3-pip python-pyaudio python3-pyaudio mpg321 pipenv python-tk
pip3 install speechRecognition wheel monotonic gtts weather-api
pipenv install requests
pipenv shell
 

