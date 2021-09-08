#!/usr/bin/python3
from subprocess import PIPE, Popen
import argparse
import re
import requests
import sys


def get_ip(ip_list):
    list_ip = [x.split(' ')[-1] for x in ip_list]
    cnt_mass = [[x, list_ip.count(x)] for x in set(list_ip)]
    result = sorted(cnt_mass, key=lambda el_mas: el_mas[1], reverse=True)
    return result


def whois(ip, whois_key):
    url = f'https://ipwhois.app/json/{ip}'
    data = {}
    if whois_key != None:
        resp = requests.get(url=url)
        data = resp.json()
    if whois_key in data:
        return data[whois_key]
    return ''


def print_unknown_element(unknown):
    print("\n\n****************************************")
    for el in unknown:
        print(f'Unknown key {el} ')
    print('\n Run programm with key --help')
    print("****************************************\n\n")


def run_command(param):
    prog_filtr = pid_filtr = ''
    command_result = []
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
        command_result = ip[0:param['count_record']]
        return command_result


def display_info(ips, whois_key):

    table = f"     \n\nip address  \tnumber of connections \twhois param ({whois_key})\n"
    table = table + "_____________________________________________________________________\n"
    for ip in ips:
        w = whois(ip[0], whois_key)
        # print ('     ', ip[0],'\t\t', ip[1], '\t',w)
        table = table + ''+str(ip[0])+'\t\t' + str(ip[1]) + '\t\t'+w+"\n"
    print(table)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="process id number")
    parser.add_argument("--n", help="programm name")
    parser.add_argument("--cnt", help="number of records")
    parser.add_argument(
        "--whois", help="Send parameter to display information from whois service. Exemple parameter 'country', 'org', 'region' e.t.c ")
    args, unknown = parser.parse_known_args()

    if len(unknown) > 0:
        print_unknown_element(unknown)

    pid = args.p
    whois_key = args.whois
    programm_name = args.n

    count_record = None
    try:
        count_record = int(args.cnt)
    except:
        pass

    if pid == None and programm_name == None:
        print('Incorrect arguments. Run programm with key --help')
    else:
        param = {
            'pid': pid,
            'programm_name': programm_name,
            'count_record': count_record
        }
        try:
            command_result = run_command(param)
            display_info(command_result, whois_key)
        except KeyboardInterrupt:
            sys.exit()
