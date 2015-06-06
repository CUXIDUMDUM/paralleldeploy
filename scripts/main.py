#!/usr/bin/env python

import os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(root)

from app import application

if __name__ == '__main__':
    application.run()
