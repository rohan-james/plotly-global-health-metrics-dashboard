# CSO-UNSC: Plotly Global Health Metrics Dashboard
A Plotly implementation of an interactive dashboard visualising the life expectancy, population growth delay, and fertility/mortality ratio based on the CSO-UNSC database.

# Instructions

## Run the below bash script to run an automated workflow
For Unix (Mac), open up a terminal after cloning the repository and run:
```
chmod +x runme.sh
./run.sh
```
For windows, open PowerShell as Administrator
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\run.ps1
```

## To manually run all scripts, run the following commands:
```
python3 -m venv .venv/
pip3 install -r requirements.txt
source .venv/bin/activate
python3 app.py
```

# Folder Structure
```
main-project-2/
└── assets/
└── callbacks/
└── components/
└── constants/
└── data/
├──app.py
├──app_instance.py
├──data_loader.py
├──index.py
├──requirements.txt
├──package.json
├──README.md
├──.env
```
---
# How to Run the dashboard server

Navigate into the project directory and run app.py:
```
python3 app.py
```
### Important : Please wait until you read 'Dash is running on http://127.0.0.1:8000/' before going to the link
---
