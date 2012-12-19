#!/bin/bash

# Runs a curl command and pretty print the xml or json response.
# All arguments to the script is pass to the curl command.

export RAW_RESPONSE=`curl -s $@`
export response=`echo "$RAW_RESPONSE" | xmllint --format  - 2> /dev/null`

if [[ -z "$response" ]] ; then
  response=`echo "$RAW_RESPONSE" | python -mjson.tool 2>/dev/null`

  if [[ -z "$response" ]] ; then
    echo "$RAW_RESPONSE"
    exit;
  fi
fi

echo "$response"

