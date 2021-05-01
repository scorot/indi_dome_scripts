# indi_dome_scripting

This repository containts the python script files I use to open and close my observatory roof with Kstars/[Ekos](https://www.indilib.org/individuals/ekos-kstars.html) using the [Dome Scripting Gateway indi driver](https://www.indilib.org/domes.html) and a prebuild garare door motor. The advantage of using the garage door prebuild system, is that there is no need to care about the programming of the motor itself. 


## What you need for those scripts

What you need is :
 * a garage door motor (I used an Avidsen motor like this [one](https://www.avidsen.com/?view=product&lang=en_US&product_id=484))
 * a Raspberrypi
 * a relay board like this [one](https://www.amazon.fr/gp/product/B0771HH6J6/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)

## How the scripts work 

On the Raspberrypi I plugged the relay board. Then I soldered two pairs of wires on the motor control board, one on the open push button pins and the other on the close push buttons pins. Then I attached them to the CH1 (open button) and CH2 (close button) of the relay board. The relays now acts just as if some one pushes the open and close button.

The scripts in this repository uses the default GPIO pin numbers assigned to this relay board. The relay Channels and corresponding pins number of the board I use are the following :

- CH1 -> pin 35
- CH2 -> pin 37
- CH3 -> pin 38
- CH4 -> pin 40


## Install and usage

Simply put all the python file in the /usr/share/indi/scripts directory. This location and the names of the scripts are the defaut values. Thus the Dome Scripting Gateway should find the files as exepected and do not need be tuned.

```shell
sudo cp *.py /usr/share/indi/scripts/
sudo chmod 755 /usr/share/indi/scripts/*.py
```

Once Ekos is started and the Dome Scripting Gateway driver is connected, the only things you have to use are the Park and Unpark buttons in Ekos. The Open and Close buttons are not used since they are effective on the shutter which is only relevent for a real rotary dome, not a roll on roof.
