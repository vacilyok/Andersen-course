#!/usr/bin/python3
from subprocess import PIPE, Popen
import argparse
import re


def get_ip(ip_list):
    list_ip = [x.split(' ')[-1] for x in ip_list]
    cnt_mass = [[x, list_ip.count(x)] for x in set(list_ip)]
    result = sorted(cnt_mass, key=lambda el_mas: el_mas[1], reverse=True)
    print(result)


def print_unknown_element(unknown):
    print("\n\n****************************************")
    for el in unknown:
        print(f'Unknown key {el} ')
    print('\n Run programm with key --help')
    print("****************************************\n\n")


def run_command(param):
    prog_filtr = pid_filtr = ''
    if param['programm_name'] != None:
        prog_filtr = f" | grep {param['programm_name']} "

    if param['pid'] != None:
        pid_filtr = f" | grep pid={param['pid']} "

    command = f"ss -tpa {pid_filtr} {prog_filtr}"
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        output = process.communicate()[0].decode("utf-8")
        pattern = r'[0-9]+(?:\.[0-9]+){3}:\w+\s+[0-9]+(?:\.[0-9]+){3}'
        parse = re.findall(pattern, output)
        ip = get_ip(parse)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="pid number")
    parser.add_argument("--n", help="programm name")
    args, unknown = parser.parse_known_args()
    if len(unknown) > 0:
        print_unknown_element(unknown)
    pid = args.p
    programm_name = args.n
    if pid == None and programm_name == None:
        print('Incorrect arguments. Run programm with key --help')
    else:
        param = {
            'pid': pid,
            'programm_name': programm_name
        }
        run_command(param)
