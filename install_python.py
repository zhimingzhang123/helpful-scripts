#!/usr/bin/python

import os
import sys
import time
import subprocess

def setUp(version):
	# make yum cache
	os.system('yum makecache')
	# install yum utils
	os.system('yum install -y yum-utils')
	# install rpm packages
	os.system('yum install -y https://centos7.iuscommunity.org/ius-release.rpm')
	# make yum cache
	os.system('yum makecache')
	# install python and pip
	os.system('yum install -y python%su'%version)
	os.system('yum install -y python%su-pip'%version)
	
	end_release = version[-1]
	print('The python version is: %s'%(os.popen('python3.%s -V'%end_release).readline().strip()))
	print('The pip version is: %s'%(os.popen('pip3.%s -V'%end_release).readline().strip()))

	python_path = os.popen('which python3.%s'%end_release).readline().strip()
	pip_path = os.popen('which pip3.%s'%end_release).readline().strip()

	subprocess.Popen("""echo "alias python3='%s'">> ~/.bashrc"""%python_path, shell=True)
	time.sleep(1)
	subprocess.Popen("""echo "alias pip3='%s'">> ~/.bashrc"""%pip_path, shell=True)
	
	#subprocess.Popen('source ~/.bashrc', shell=True, executable="/bin/bash")
        os.system('source ~/.bashrc')

	print('Now you can use `python3` enter it \nyou can use `pip3` install packages')

if __name__ == '__main__':
	print('Please input the version to install pyhton: \n(example: if you want install pyhton3.4 you can input 34)')
	version = eval(raw_input())
	if version > 36 or version < 30:
		raise 'Invalid python version' 
	setUp(str(version))
