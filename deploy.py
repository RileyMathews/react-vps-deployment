# script to automate react deployment
import os, json, subprocess, shutil

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

# remove current build folder if exists
if os.path.exists(build_folder):
    shutil.rmtree(build_folder)

# run app build
subprocess.check_call('npm run build', shell=True)
print('app built')

# run command
command = f'rsync -avz {build_folder} {username}@{vps_ip}:{vps_directory}'
print(command)
subprocess.check_call(command.split(), shell=True)
