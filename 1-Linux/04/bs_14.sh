#!/bin/bash

HOST="google.com"

ping -c 1 $HOST > /dev/null && echo "$HOST is reachable" || echo "$HOST is not reachable"
