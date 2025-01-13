# !/bin/bash

cd ./Front
npm run build
cd ../Back
pip3 install -r requirements.txt 