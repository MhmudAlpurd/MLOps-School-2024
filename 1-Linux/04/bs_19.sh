#!/bin/bash

HOST="google.com"

while ping -c 1 $HOST > /dev/null   
    do 
       echo "$HOST is reachable!"
       sleep 5
    done



