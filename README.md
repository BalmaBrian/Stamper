# Stamper - PNG to STL Maker
Stamper is a program that makes stamp stl's files for 3D printing. Simply give the program a black and white png file and it will make a stl file you can throw at a slicer and 3D print.
## Getting Started
The first thing you need is a linux system or a linux VM. The software used is Python 3 and OpenSCad.

### Installing OpenSCad for Ubuntu 18.04 - [Tutorial Here](http://ubuntuhandbook.org/index.php/2019/01/install-openscad-ubuntu-18-10-18-04/)
1. Open terminal either via **Ctrl+Alt+T** keyboard shortcut or from software launcher.
When it opens, paste following command and run to add the PPA:
```bash
sudo add-apt-repository ppa:openscad/releases
```
2. apt-get the update and then upgrade
```bash
sudo apt-get update
sudo apt-get upgrade
```
3. Install OpenSCad
```bash
$ sudo apt-get install openscad
```

### Uninstalling OpenSCad on Ubuntu 18.04
1. Run the following command
```bash
$ sudo apt-get remove --autoremove openscad
```

### Testing Stamper
Once you clone the repository there will be a python file called `ImageManipulation.py`. Run the `python3` command with the destination being the test file and the resulting output will be stored in a directory called `TestOutput/`.
```bash
$ python3 ImageManipulation.py
```
After you run that the resulting output should look cool! If there is an error then make sure you have OpenSCad installed and or you are using Python 3.

### Running Stamper
To run stamper put any small 300x300 png or jpeg file in the directory `TurnsFilesB&W/` and run the python command:
```bash
$ python3 main.py
```
The output stl files will be in the `FilesOut/` Directory.

### Built with
- [OpenSCad](https://www.openscad.org/) - The Programmers Solid 3D Modeller
- [Python 3](https://www.python.org/) - Programming Language

### Authors
- Brian Almaguer
- My Sanity
- Jesus
- Coding Gods

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwODI2NDYwMiwxNDk1ODA5OTU1LDE1MT
ExNTIyMiw1NzQ2MTEyMjFdfQ==
-->