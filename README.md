
![logo](media/panoptes_logo_no_background.png)

### An OSINT toolbox

## Authors

- [@ydhemtek](https://www.github.com/ydhemtek)

- [@edoigtrd](https://www.github.com/edoigtrd)


## Summary

Panoptes is a collection of several osint tools, making it easier to find open source information.

Some modules use tools created by [@megadose](https://www.github.com/megadose)

-  Coded with Python 3
-  Builtins modules uses Tor proxy
-  Use [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

# Modules

Panoptes is composed of several modules:

### 1. Megadose
 Megadose module is a collection of tools created by [@megadose](https://www.github.com/megadose)
 - [Holehe](https://github.com/megadose/holehe)
 - [Toutatis](https://github.com/megadose/toutatis)
 - [Ignorent](https://github.com/megadose/ignorant)

### 2. Immatriculation
 Immatriculation module is a tool to find information about a vehicle using its license plate number.
 It only works in France for the moment.

### 3. Open streets maps
 Open streets maps is a module used to find two closest instances of a given address.
 Example: Fnac + McDonalds will find places near a Fnac and a McDonalds.

### 4. Username
 Username module is a tool that search usernames on different social medias.
 It is inspired on [sherlock](https://github.com/sherlock-project/sherlock/)

### 5. Name
 Name module takes a name and a surname as input and search the address of the person
 It uses [PagesJaunes](https://www.pagesjaunes.fr/) and [PagesBlanches](https://www.pagesblanches.fr/) so it only works in France for the moment.

## installation

```bash
[user]$ git clone git@github.com:ydhemtek/Panoptes.git
[user]$ cd Panoptes
[user]$ python3 setup.py install

```

> To uninstall the package, run the following command:
> ```bash
> [user]$ sudo python3 setup.py uninstall
> ```

## Example / Run

After installing on Linux, you can run the program by typing the following command in the terminal:

```bash
[user]$ ./panoptes
```

Unfortunately Windows installer does not add Penoptes to PATH, so you have to run it from the directory where it is installed.

```bash
> run.bat
```

## Error case / Warning

# type of recurring error :

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

# ⚠️ make sure you always have the latest version of chrome. ⚠️

Install [Chrome](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjpx8L2t5P-AhWO91EKHcmNCpwYABABGgJ3cw&ohost=www.google.com&cid=CAESbeD26ibCdTRUJqYiRxupSrotoeEW43uIMDFr5NxbEvmKSNfCzGPk7A_XR0TNvRdXJG-tyBYkXn_1raGDx7TQ_zt5wwWomctnMa89_uk2WjoIgfCNBbwEsAx6UeIrP2597-2rKVTl42Cx9sHqTJg&sig=AOD64_3lXi44u6AXISAd8yXXsUxajE8grg&adurl&ved=2ahUKEwiy17v2t5P-AhX4UaQEHUQ2AyQQqyQoAHoECAgQCw) on the offical page (link for Debian/Ubuntu/Fedora/openSUSE.)

# For update Chrome :

For Fedora :

```bash
rpm -qa | grep google-chrome
```
Look at see if you can find the installed chrome package, maybe not only one, just choice which one you want to uninstall, enter:
```bash
rpm -e <chrome-package-name-here>
```
For example:
```bash
rpm -e google-chrome-unstable-41.0.2224.3-1.x86_64
```
know install the package :

```bash
rpm -i "google-chrome-stable_current_x86_64(1).rpm" 
```

# ⚠️ if the error persists, don't worry, simply restart the chosen module until a loading bar is displayed ⚠️