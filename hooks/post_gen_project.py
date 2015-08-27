# -*- coding: utf-8 -*-
import os
import shutil

project_directory = os.path.realpath(os.path.curdir)

if '{{cookiecutter.support_windows}}'.lower() != 'y':
    shutil.rmtree(os.path.join(project_directory, 'appveyor'))
