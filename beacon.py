import subprocess, shlex
import json
import csv
import os
import time

def get_output(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out

def get_json(args):
    '''
    Gets json from termux api commands
    '''
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return json.loads(out.decode('utf8'))

def termux_wifi_scaninfo():
    '''
    wrapper for termux api command
    '''
    LOG_CMD = "termux-wifi-scaninfo"

    args = shlex.split(LOG_CMD)
    return get_json(args)


def termux_wifi_connection_info():
    CMD = "termux-wifi-connectioninfo"
    args = shlex.split(CMD)
    return get_json(args)

def termux_wifi_enable(state):
    CMD = f"termux-wifi-enable {str(state).lower()}"
    args = shlex.split(CMD)
    return get_output(args)


def wifi_connected():
    result =  termux_wifi_connection_info()
    if result['supplicant_state'] == "COMPLETED":
        return True
    return False


def json_to_csv(output):
    sheet = []
    sheet.append(list(output[0].keys()))
    for obj in output:
        row = []
        for keyword in sheet[0]:
            try:
                row.append(obj[keyword])
            except KeyError:
                row.append(None)
        sheet.append(row)
    return sheet

def pprint_sheet(sheet):
    for line in sheet:
        print(' '.join([str(i) for i in line]))
    

def flushed_write(filename ,sheet):
    with open(filename, 'w', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)

        for row in sheet:
            writer.writerow(row)

def append_write(filename ,sheet):
    with open(filename, 'a', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        
        sheet.pop(0)
        for row in sheet:
            writer.writerow(row)
            
def log_wifi_scaninfo(filename):
    output = termux_wifi_scaninfo()
    if output != []:
        sheet = json_to_csv(output)
        #pprint_sheet(sheet)

        # if log file exists append to it else: create it
        if os.path.exists(filename):
            append_write(filename ,sheet)
        else:
            flushed_write(filename ,sheet)
    else:
        goto_wifi_settings()
        time.sleep(4)
        log_wifi_scaninfo(filename)

def goto_wifi_settings():
    CMD='am start -n com.android.settings/com.android.settings.wifi.WifiSettings'
    #args = shlex.split(CMD)
    os.system(CMD)
    
def main():
    WIFI_STATE = wifi_connected()
    if not WIFI_STATE:
        termux_wifi_enable(True)
        # This gets the scanning API working
        # the only way I know right now
        goto_wifi_settings()
        time.sleep(5)

    filename = 'beacons.csv'
    log_wifi_scaninfo(filename)

    if not WIFI_STATE:
        termux_wifi_enable(False)

main()
