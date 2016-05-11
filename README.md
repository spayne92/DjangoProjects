# DjangoProjects
Repository of multiple Django projects.

Includes a vagrant file with provisioning for an Ubunutu 64 (trusty 64) server box with 
python3.4, pip3, and django preinstalled.

Command 'vagrant ssh' will default into the shared vagrant folder, based on addition 
to .bashrc file in privisioned box.

Alias also premade for command 'runserver' which will run the current django web project (from within its directory), 
accessible from localhost:8080 in the host machines web browser.

Alias 'home' will return to the top level of the shared vagrant directory while in vagrant shell.

All this requires having VirtualBox and Vagrant installed on your machine. 

Individual directories like "Tutorial" will hold seperate django projects.
