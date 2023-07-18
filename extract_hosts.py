import requests
import json
import os

os.remove("c:/Users/ac43264/documents/zabbixagents.txt")
file = open("c:/Users/ac43264/documents/zabbixagents.txt", "a")

# NA
zabbix_na_url = "https://zabbixna.na.goodyear.com/api_jsonrpc.php"
zabbix_na_token = "c401f06a5e4b782196d95fb22649977228ef1b276f1f393283356f12f28314f8"  # NA

zabbix_test_url = "https://zabbixnatest.na.goodyear.com/api_jsonrpc.php"
zabbix_test_token = "5ea91b279991ed97e627e00869aada09"  # Test

# EMEA
zabbix_emea_url = "https://zabbixemea.ec.goodyear.com/api_jsonrpc.php"
zabbix_emea_token = "26f747cd2edb25a15c12435f0c0ecc5d83c3f23bed3779622d120933a5115efe"  # EMEA


def zabbix_get_hosts(zabbix_url, zabbix_token):
    print(f"Getting from {zabbix_url}")

    # Zabbix Payload

    data = {

        "jsonrpc": "2.0",

        "method": "host.get",

        "auth": zabbix_token,

        "id": 1,

        "params": {

            "output": ["host", "host_id"]

        },

    }

    response = requests.post(zabbix_url, json=data, verify=False)  # Less Secure
    # print(response.text)
    json_data = json.loads(response.text)
    for json_item in json_data['result']:
        zbx_host = json_item['host']
        if "." in zbx_host:
            zbx_host = zbx_host.split(".")[0]
        print(zbx_host, file=file)


zabbix_get_hosts(zabbix_emea_url, zabbix_emea_token)
zabbix_get_hosts(zabbix_na_url, zabbix_na_token)
file.close()
