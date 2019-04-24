#!/bin/sh
cd /Users/demo &&

echo `date` >> /Users/demo/log
/usr/local/bin/python3 /Users/steven/graDesign/main.py
echo 'finish' >> /Users/demo/log