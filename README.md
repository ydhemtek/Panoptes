
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