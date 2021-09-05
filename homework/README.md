## Description
___
Simple falsk server for homework for the Andersen course. The flask server is installed on a remote host using ansible playbook. 

## Requirements 
```
Git client must be installed on your pc 
```

## Install 
```
Run command:
1. git clone https://github.com/vacilyok/Andersen-course.git
2. cd Andersen-course/homework/
3. vi  hosts.txt  then change ip address and ssh user, ssh password, sudo password.
4. ansible-playbook playbook.yml
```

Wait a while! In your browser, go to http://remote_host_ip 
