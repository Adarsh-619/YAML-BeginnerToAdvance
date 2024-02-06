import yaml
import json
import pprint
import os
from termcolor import colored


files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)
          and (f.endswith('yaml') or f.endswith('yaml'))]

fileName = ""

print("Please select the file:")
for i, f in enumerate(files):
    print(str(i + 1) + ". " + f)

selectedFile = int(input())
try:
    fileName = files[selectedFile - 1] 
except IndexError:
    raise Exception("Invalid input. Please try again")

print("**************")

with open(fileName, 'r') as f:
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
        multilineDoc = ""
        for ind, item in enumerate(data):
            if (fileName == "yaml_basics.yaml" and ind == 1):
                multilineDoc = item['multiline']
            print(f'Document - {ind + 1}\n**************')
            print(json.dumps(item, indent=4))
            print('\n**************\n')

        if fileName == "yaml_basics.yaml":
            print("Printing the multiline:\n" + multilineDoc)
    except yaml.YAMLError as exc:
        print(exc)
    except TypeError as exc:
        print(colored(exc, 'red'))
        
