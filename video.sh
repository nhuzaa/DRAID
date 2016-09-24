#!/bin/bash
ffserver /etc/ffserver.conf & ffmpeg -i /dev/video0 -threads 0 http://localhost:7777/feed1.ffm && fg
