"""
This module provides functionality to parse the yaml to json.

It makes use of the yaml module to process the yaml file and converts it into json. 
The repository currently has 3 files which covers all the basics of YAML

Author: Adarsh Patra
Date: February 6, 2024
"""


import json
# import pprint
import os
import yaml
from termcolor import colored


files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)
         and (f.endswith('yaml') or f.endswith('yaml'))]

FILE_NAME = ""

print("Please select the file:")
for i, f in enumerate(files):
    print(str(i + 1) + ". " + f)

selectedFile = int(input())
try:
    FILE_NAME = files[selectedFile - 1]
except IndexError as exc:
    raise IndexError('Invalid input. Please try again') from exc

print("**************")

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    # data = yaml.load(f, Loader=yaml.SafeLoader)
    try:
        # data = yaml.safe_load(f) # For single document
        data = yaml.safe_load_all(f)
        # Print the values as a dictionary
        # Single document
        # print(json.dumps(data, indent = 4))
        # pprint.pprint(data) # Print json in pretty format

        # print("Printing the multiline:\n" + data['multiline'])

        # Multiple Document
        MULTILINE_DOC = ""
        for ind, item in enumerate(data):
            if (FILE_NAME == "yaml_basics.yaml" and ind == 1):
                MULTILINE_DOC = item['multiline']
            print(f'Document - {ind + 1}\n**************')
            print(json.dumps(item, indent=4))
            print('\n**************\n')

        if FILE_NAME == "yaml_basics.yaml":
            print("Printing the multiline:\n" + MULTILINE_DOC)
    except yaml.YAMLError as exc:
        print(exc)
    except TypeError as exc:
        print(colored(exc, 'red'))
