#!/bin/bash

read -p "write your name: " ANSWER

if [ "$ANSWER" = "admin" ]
     then 
         echo "you are confirmed"

else
    echo "you are wrong"

fi
