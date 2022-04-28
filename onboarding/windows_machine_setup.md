# **Windows Machine Setup**

This is the setup guide for Window users that includes the software with instructions on "How to".

We will be going over:
 - [Windows Update](#windows-update)
 - [WSL](#wsl)
 - [Docker](#docker)
 - [GitHub](#github)
 - [Code Editor](#code-editor)

# **Setup**

This documentation is to help you in setting up everything that will be needed all in one document.

Please update if any step is no longer up-to-date.

## Windows Update

It is important to have all the security up-to-date and some platforms require it as well.  This is the first step to ensure no issues come up with the proceeding installations.

You can install security updates by clicking the "**start**" menu button and searching for "**Settings**".

Following the category list on the left side, select "**Windows Update**" and click the "**Check for updates**" button if needed.

Rebooting may be necessary.

## WSL

### **Installation**

[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) is mainly used for engineering.

To [install](https://docs.microsoft.com/en-us/windows/wsl/install), open the cmd/terminal and type:

    wsl --install

There is a list of available Linux distros that can be installed, you can check these by the following command:

    wsl --list --online

To install the distro:

    wsl --install -d <DistroName>

Once installation is completed, you can access the WSL by typing:

    wsl

Please note:
 - wsl installation will ask for UNIX username, it will only accpet lowercase characters.
 - The UNIX password will be requested when root access is required.

### **Update**

Once connected to your wsl, please update your distro:

    sudo apt update && sudo apt upgrade

## Docker

### **Installation**

[Development platform](https://www.docker.com/) that contains configuration/environmental specifications per project.

To install navigate to Docker's [Getting Started](https://www.docker.com/get-started/) page and select the "**Download for Windows**" option.

You should get a file called:

    Docker Desktop Installer.exe

Open the executable file and run through all of the installation settings.

### **Sign into Docker Desktop**

Create an account if you don't have one.

Please see [Docker Docs](https://docs.docker.com) for more information.

## GitHub

WSL already comes with Git, the only thing that is required it to signing utilizing the GitHub Token.  Due to GitHub's security, you can only generate tokens after having 2FactorAuthentication setup.

### **GitHub 2FA**

Navigate to your "**[GitHub Settings Security](https://github.com/settings/security)**" page and click the Two-factor methods and follow their instructions.

After this is setup, proceed to the following step.

### **GitHub Token**

To create the token, please navigate to your [GitHub Settings](https://github.com/settings/tokens) page:

    https://github.com/settings/tokens

Click on the "**Generate new token**" button.

Under "**Selected scopes**" the first section that covers "**repo**" should be fine unless specified otherwise.

Please note: Once these steps are fulfilled can you utilze Git in WSL.

# Code Editor

Code editors can range from preferences, which is not a problem.

The only issue that can come up is utilizing newer or different versions of these.  For example: Visual Code Insighter was not detected when attempting to access it inside WSL using.

    code .

It was still not being access even after checking the environmental PATH settings.

## Decision

To have a compact "batteries included" installation for oncoming Window's users.

## Consequences

This file should help assist all oncoming Window's users.
