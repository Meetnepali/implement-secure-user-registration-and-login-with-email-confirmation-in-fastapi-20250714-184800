#!/bin/bash
set -e
# Install required system packages
apt-get update
apt-get install -y python3 python3-pip python3-venv build-essential libffi-dev libpq-dev gcc
# Setup python venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
