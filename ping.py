import os

hostname = '192.168.32.39'
ping = 4
response = os.system(f'ping {hostname} -c{ping}')