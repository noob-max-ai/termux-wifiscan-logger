![](https://img.shields.io/github/license/noob-max-ai/termux-wifiscan-logger) 
![](https://img.shields.io/github/stars/noob-max-ai/termux-wifiscan-logger)
![](https://img.shields.io/github/issues/noob-max-ai/termux-wifiscan-logger)
![](https://badgen.net/badge/icon/terminal?icon=terminal&label)
![](https://badgen.net/badge/icon/awesome?icon=awesome&label)
# termux-wifiscan-logger
User scripts to log wifiscan info to csv file.

# Motivation
I built this to collect data about wifi beacons around me. I will add location related stuff later.
The motivation was to analyze data around me.

# Installation
```bash
git clone https://github.com/noob-max-ai/termux-wifiscan-logger/ --depth=1
cd termux-wifiscan-logger
python beacon.py
```
# Setup with termux widgets

```sh
mv beacon.py ~/
chmod +x beacon.sh
mv beacon.sh ~/.shortcuts/

```

# How it Works

If wifi is off
+ Turns on Wifi
+ Logs wifi beacons to beacons.csv file
+ Turn off wifi
If wifi is on
+ Logs wifi beacons to beacons.csv file

# Tested on
| Application Version | CPU architecture | Android version |
|---------------------|------------------|-----------------|
| 0.117               | aarch64          | 10              |
|                     |                  |                 |
|                     |                  |                 |
