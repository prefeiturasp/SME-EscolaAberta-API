#!/bin/sh
PATH=/bin:/sbin:/usr/bin:/usr/sbin; export PATH;
git pull origin master
git status
git add .
git add src/*
git commit -m "ok $1"
git push -u origin master
git status




