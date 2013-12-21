#!/bin/bash

# coding=utf-8

"true" '''\'
exec "$(dirname $0)/venv/bin/python" "$0" "$@"
'''

import os
import sys


if  __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "famille.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
