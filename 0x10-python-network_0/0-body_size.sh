#!/bin/bash
# Takes in a URL, sends a request to URL and body size response
curl -s "$1" | wc -c
