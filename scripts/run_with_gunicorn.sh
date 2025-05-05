#!/bin/bash

# Run pybarsys with gunicorn (intended for production use together with nginx or apache)
set -eux

# cd to root folder
cd "${0%/*}/.."

# Prepare the application
scripts/prepare_pybarsys.sh

# Start Gunicorn with the custom configuration
gunicorn --config gunicorn_config.py --bind :8000 pybarsys.wsgi:application
