#!/bin/sh
source venv/bin/activate
export FLASK_APP="run.py"
export SECRET="thisISsomeSECRETwords"
export APP_SETTINGS="development"
export DATABASE_URL="postgresql://urestful:marimakan@172.17.0.2/restful"
