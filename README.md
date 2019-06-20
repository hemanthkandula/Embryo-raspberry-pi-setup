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




Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
