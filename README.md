![logo](media/panoptes_logo_no_background.png)

# Panoptes: An OSINT Toolbox

## Authors

- [@ydhemtek](https://www.github.com/ydhemtek)
- [@edoigtrd](https://www.github.com/edoigtrd)

## Summary

Panoptes is a collection of OSINT tools designed to make it easier to find open-source information.

Some modules use tools created by [@megadose](https://www.github.com/megadose).

- Coded with Python 3
- Built-in modules use Tor proxy
- Uses [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

## Modules

Panoptes is composed of several modules:

### 1. Megadose

The Megadose module is a collection of tools created by [@megadose](https://www.github.com/megadose):

- [Holehe](https://github.com/megadose/holehe)
- [Toutatis](https://github.com/megadose/toutatis)
- [Ignorent](https://github.com/megadose/ignorant)

### 2. Immatriculation

The Immatriculation module is a tool for finding information about a vehicle using its license plate number. It currently only works in France.

### 3. OpenStreetMaps

The OpenStreetMaps module is a tool for finding the two closest instances of a given address. For example, "Fnac + McDonalds" will find places near a Fnac and a McDonalds.

### 4. Username

The Username module is a tool for searching usernames on different social media platforms. It is inspired by [sherlock](https://github.com/sherlock-project/sherlock/).

### 5. Name

The Name module takes a name and a surname as input and searches for the person's address. It uses [PagesJaunes](https://www.pagesjaunes.fr/) and [PagesBlanches](https://www.pagesblanches.fr/), so it only works in France at the moment.

## Installation

```bash
[user]$ git clone git@github.com:ydhemtek/Panoptes.git
[user]$ cd Panoptes
[user]$ python3 setup.py install
```

To uninstall the package, run the following command:

```bash
[user]$ sudo python3 setup.py uninstall
```

## Usage

After installing on Linux, you can run the program by typing the following command in the terminal:

```bash
[user]$ ./panoptes
```

Unfortunately, the Windows installer does not add Panoptes to PATH, so you have to run it from the directory where it is installed:

```bash
> run.bat
```

## Error Cases/Warnings
### Recurring Error Types

```bash
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot connect to chrome at 127.0.0.1:46973
from session not created: This version of ChromeDriver only supports Chrome version 112
Current browser version is 111.0.5563.146
Stacktrace:
#0 0x55bf0fd28fe3 <unknown>
#1 0x55bf0fa67d36 <unknown>
#2 0x55bf0fa9548c <unknown>
#3 0x55bf0fa8c352 <unknown>
#4 0x55bf0faceaf7 <unknown>
#5 0x55bf0face11f <unknown>
#6 0x55bf0fac5693 <unknown>
#7 0x55bf0fa9803a <unknown>
#8 0x55bf0fa9917e <unknown>
#9 0x55bf0fceadbd <unknown>
#10 0x55bf0fceec6c <unknown>
#11 0x55bf0fcf84b0 <unknown>
#12 0x55bf0fcefd63 <unknown>
#13 0x55bf0fcc2c35 <unknown>
#14 0x55bf0fd13138 <unknown>
#15 0x55bf0fd132c7 <unknown>
#16 0x55bf0fd21093 <unknown>
#17 0x7f8f5da8cded start_thread
```

# ⚠️ Make sure you always have the latest version of Chrome. ⚠️

To ensure that you have the latest version of Chrome, install it from the official page [here](google.com/chrome/) . If you are using Debian, Ubuntu, Fedora, or openSUSE, use the corresponding link provided on the page.

## To update Chrome

For fedore :

- Check which version(s) of Google Chrome you have installed:
```bash
rpm -qa | grep google-chrome
```
- Choose the version you want to uninstall and execute the following command:
```bash
rpm -e <chrome-package-name-here>
```
For example:
```bash
rpm -e google-chrome-unstable-41.0.2224.3-1.x86_64
```

- Install the latest version of Chrome:
```bash
rpm -i "google-chrome-stable_current_x86_64.rpm" 
```

### ⚠️ If the error persists, simply restart the selected module until a loading bar is displayed. ⚠️
