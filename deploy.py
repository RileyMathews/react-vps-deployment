# script to automate react deployment
import os, json

# get working directory of folder
working_directory = os.path.abspath(os.path.curdir)
deployment_json = f'{working_directory}/deployment.json'
build_folder = f'{working_directory}/build'
print(working_directory)

# open up json file with deployment information
with open(deployment_json) as file:
    data = json.load(file)

    vps_ip = data['ip_address']
    username = data['username']
    vps_directory = data['vps_directory']

print(f'deploying files at {build_folder} to {username}@{vps_ip}:{vps_directory}')

# run command
command = f'rsync -avz {build_folder} {username}@{vps_ip}:{vps_directory}'
print(command)