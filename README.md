# Multi Guide for replit
## What is multi?
>Multi is a bash command made for ease of use.
>Multi is made to make having 2 or more languages on the same repl easy with just a few commands.
## Installation:
### Starting anew:
Fork this repl or use the template and boom! you should have it working. If the multi commands don't work run the commands below:
```bash
chmod u+x setuptools.sh
eval `./setuptools.sh`
```
### Adding to a old repl:
First clone my github via:
```bash
git clone -b clone --single-branch https://github.com/thatrandomperson5/replit-multi.git
```
After you clone into your repl run these command:
```bash
cd replit-multi
chmod u+x setuptools.sh
eval `./setuptools.sh`
```
Boom! Now you should have access to multi anywhere in your project

## Commands:
### Multi:
```sh
multi
```
Lists all commands
### List:
```sh
multi list
```
Requires one argument of:
* `-I (--installed)`
* `-N (--ninstalled)`
* `-A (--all)`
  
And lists all of the specifed category.
### Version
```sh
multi version
```
Lists version details.
### Install
```sh
multi install <lang> 
```
**(Java not yet supported)**

Installs the language specified by `<lang>`
To see the languages run this command:
```sh
multi list -A
```
### Uninstall
```sh
multi uninstall <lang>
```
Uninstalls a language.
## Dangerous Commands:
### Update
```sh
multi update
```
An attempt at auto updates.
## Problems:
### Binary error:
`cannot execute binary file` Error.

Fix should be to replace all `multi` in commands with `multi.bin`
### Multi not found error:
Run setuptools again depending on how you installed multi.
