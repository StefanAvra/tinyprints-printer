# tinyprints-printer
Printer code for tinyprints, that downloads submissions and prints them.

This script calls the api of [tinyprints](https://github.com/StefanAvra/tinyprints) to close voting for the currently highest submission and prints via serial connection on the thermal printer. My thermal printer is connected to a Raspberry Pi, so this is executed on that Pi.

## Usage

Clone this repo and cd into it.

Create a venv and install requirements
```sh
python3 -m venv venv
pip install -r requirements.txt
```
You can set the environment variabel for the api key like this
```sh
export TINYPRINTS_API_PASSWORD="your secret pw"
```
You probably want to create a cron job to execute the script. Don't forget to add the env var as well.
for example everyday at 20:00 UTC:
```sh
0 20 * * * export TINYPRINTS_API_PASSWORD="your secret pw"; /home/pi/tinyprints-printer/run.sh
```