# -*- coding: utf-8 -*-
import csv
import os


def get_arp_table():

    with os.popen('arp -a') as arpt:
        names = [
            'IP address', 'HW type', 'Flags', 'HW address', 'Mask', 'Device'
        ]  # arp 1.88, net-tools 1.60

        reader = csv.DictReader(
            arpt, fieldnames=names, skipinitialspace=True, delimiter=' ')

        next(reader)  # Skip header.

        return [block for block in reader]


ARPTABLE = get_arp_table()
for i in range(len(ARPTABLE)):
    print(ARPTABLE[i])
