#!/bin/bash
# Json Post
curl -s -H "Content-Type: application/json" -d "$(cat "$2") "$1"
