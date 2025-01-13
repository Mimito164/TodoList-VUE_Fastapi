# !/bin/bash

cd ./Front
npm install
npm run build
cd ../Back
pip3 install --upgrade pip
pip3 install -r requirements.txt 