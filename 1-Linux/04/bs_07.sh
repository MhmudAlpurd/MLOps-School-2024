#!/bin/bash

MYHOST="$HOSTNAME"

if [ "$MYHOST" = "GUEST_USER" ]
   then
       echo "$MYHOST is not secure"

elif [ "$MYHOST" = "mhmud" ]
   then
       echo "$MYHOST is the best for you"
else
    echo "choose another server"

fi
