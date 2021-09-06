## Description

---

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
3. vi  hosts.txt  then change ip address
4. vi playbook.yml and insert ansible-vault encript string in vars ansible_ssh_pass and ansible_sudo_pass.
5. run ansible-playbook playbook.yml --ask-vault-pass
```

Wait a while! In your browser, go to http://remote_host_ip
