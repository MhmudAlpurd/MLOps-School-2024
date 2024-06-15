#!/bin/bash

MYHOST="$HOSTNAME"

if [ "$MYHOST" = "guest_host" ]
   then
       echo "$MYHOST is not secure"
else
    echo " $MYHOST  is the best server for you"
fi
