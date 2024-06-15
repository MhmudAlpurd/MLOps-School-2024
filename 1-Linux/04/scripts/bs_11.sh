#!/bin/bash

HOST="google.com"
HOST_Filtered="Facebook.com"

#ping -c 1 $HOST
ping -c 1 $HOST_Filtered

if  [ "$?" -eq "0" ]
    then 
         echo "$HOST_Filtered is reachable, continue"

else
    echo "$HOST_Filtered  is not reachable, send an email to ADMIN"

fi
