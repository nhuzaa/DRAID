#!/bin/bash
python DRAIDservo/servo/sock.py & python DRAIDservo/manage.py runserver 0:5555 && fg
