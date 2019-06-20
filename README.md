# Embryo raspberry pi setup

Setup instructions for raspberry pi for Embryo standalone device

## Setup Instructions

Download [raspbian OS](https://www.raspberrypi.org/downloads/raspbian/) and install to SD card.

If using windows use [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/)

after installing open cmd and navigate to boot Volume

```bash
notepad ssh.
```
Save the `ssh.` file to enable ssh

```bash
notepad wpa_supplicant.conf
```
save the following in the `wpa_supplicant.conf` file.

```bash
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
 ssid="Shafiee Lab Team"
 scan_ssid=1
 psk="Hslab2017"
 key_mgmt=WPA-PSK
}

```

Now boot the raspberry pi it should be connected to WiFi network.


Copy `Embryo\` folder from this repo to the home directory usually at `/home/pi/`


## Package Installations

First, update the available packages by typing the following command into the Terminal:

```bash
sudo apt-get update
```

#### Install Python3 and virtualenv
```
sudo apt-get install python3-pip


sudo su
pip3 install virtualenv 
exit

cd ~/Embryo/scripts
virtualenv py3
source py3/bin/activate
pip3 install picamera flask
```





### Install apache2 and Flask server



Then, install the `apache2` package with this command:

```bash 
sudo apt-get install apache2 -y
sudo apt-get install libapache2-mod-wsgi-py3
```

## Setup Flask server



Now disable default website with the following command:

```bash
cd /etc/apache2/sites-available/
sudo a2dissite 000-default.conf 
```


