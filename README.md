# indi_dome_scripting

This repository containts the python scripts file I use to open en close my observatory roof using the Dome Scripting Gateway indi driver.


## What you need for those scripts
I motorised my roll on roof with a garage door motor. I used an Avidsen motor like this one https://www.avidsen.com/?view=product&lang=en_US&product_id=484. The advantage is thats I didn't have to care about the programming of the motor itself.

On my raspberry pi I pluged a relay board like this : https://www.amazon.fr/gp/product/B0771HH6J6/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1. Then I soldered the wires on the motor control board on the push button pins and attacehd them to the CH1 (open button) and CH2 (close button) of the board. 

## How the scripts work 
The scripts in this repository uses the default GPIO pin numbers assigned to this relay board. The relays acts just as if some one pushes the open and close button.

## Install

Simply put all the python file in the /usr/share/indi/scripts directory. This location and the names of the scripts are the defaut values. Thus the Dome Scripting Gateway should find the files as exepected and should not be tuned.
