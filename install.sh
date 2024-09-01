#!/bin/bash

INDI_SCRIPTS_DIR=/usr/share/indi/scripts

if [ ! -d $INDI_SCRIPTS_DIR ]; then
	echo "Target directory $INDI_SCRIPTS_DIR does not exists."
	echo "Is indi installed ?"
	exit 1
fi

echo "Install scripts in $INDI_SCRIPTS_DIR ..."
for i in *.py;
do
	install -m755 ./$i $INDI_SCRIPTS_DIR/$i
        echo "$i installed."
done

