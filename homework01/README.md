## Description

---

Simple falsk server for homework for the Andersen course. The flask server is installed on a remote host using ansible playbook.

## Requirements

```
1. Git client must be installed on your public
2. Public key should be generated on your pc

```

## Install

```
Run command:
1. git clone https://github.com/vacilyok/Andersen-course.git
2. cd Andersen-course/homework01/
3. vi  hosts.txt  then change ip address
4. vi group_vars/debian.yaml and change value ansible_ssh_pass and ansible_sudo_pass.
5. run ansible-playbook playbook.yml
```

Wait a while! In your browser, go to http://remote_host_ip
