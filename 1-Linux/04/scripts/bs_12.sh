#!/bin/bash


HOST="facebook.com"

ping -c 1 $HOST > /dev/null

if [ "$?" -ne "0" ]
   then
        echo "$HOST is not reachable, ..."
fi
