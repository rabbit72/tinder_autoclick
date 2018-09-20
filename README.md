# Tinder autoclicker

This is autoclicker for Tinder.com 

This script use authentication with mobile phone, you have to input code by
yourself.

The first time you have to login by yourself and create account.

This clicker use Google Chrome browser. 

# How to install

Your system must have Google Chrome and
Chrome Driver (https://sites.google.com/a/chromium.org/chromedriver/downloads)

Put this file to ```/usr/bin/ ```

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt
```

If you use ```pipenv```:

```bash
$ pipenv --three sync
```
# Quick start

```bash
$ python3 clicker.py [--like <number>] <phone_number>
```

If you use ```pipenv```:
```bash
$ pipenv run python python3 clicker.py [--like <number>] <phone_number>
```
Format phone number 9121234567 (without country code)

```--like``` is 10 by default 

Running on Windows is similar.

*(Possibly requires call of 'python' executive instead of just 'python3'.)*