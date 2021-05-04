#!/bin/sh

echo "Enter the new version number:"
read new_version
cat setup.py | sed -e 's/version="[0-9.]*"/version="$new_version"/'
