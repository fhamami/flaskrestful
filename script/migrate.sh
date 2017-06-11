#!/bin/sh
echo "Please enter message: "
read msg
python manage.py db migrate -m $msg
