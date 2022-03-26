# termux-wifiscan-logger
User scripts to log wifiscan info to csv file.

# installation
```bash
git clone https://github.com/noob-max-ai/termux-wifiscan-logger/ --depth=1
cd termux-wifiscan-logger
python beacon.py
```
# setup with termux widgets

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
