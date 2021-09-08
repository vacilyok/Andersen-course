## Description

---

The script displays a list of established connections. To get a list of established connections in the script, you must pass the pid key or name program.

## Requirements

```
python 3
```

## List keys

```
--p - process id number
--n - programm name
--cnt - number of records
--whois - Send parameter to display information from whois service. Exemple parameter 'country', 'org', 'region' e.t.c
```

## Exemple

```
python3 conn.py --p=904 --whois=org --cnt=3
or
python3 conn.py --n=firefox --whois=org --cnt=3
```
