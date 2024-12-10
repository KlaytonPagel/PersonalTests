#!/bin/bash

REPO_PATH=$1
PROJECT_NAME=$2
APP_NAME=$3

cd $REPO_PATH
success="Your branch is up to date with 'origin/main'."
git fetch origin main
status=$(git status | grep "$success")
if [ "$status" == "$success" ]; then
  echo "up to date"
  exit 0

else
  echo "not up to date"
  git stash
  git reset --hard origin/main

  cd "$REPO_PATH/$PROJECT_NAME/$APP_NAME"
  npm install
  npm run build

  cd "$REPO_PATH/$PROJECT_NAME"
  kill $(ps aux | grep 'manage.py' | awk '{print $2}')
  python3 manage.py runserver 0.0.0.0:80
fi
