# Champ Foronda
# Web Crawler 1.0
# Created: April 20th, 2018

import os

# Each website crawl, create new project


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project: ' + directory)
        os.makedirs(directory)

create_project_dir(test)
