#!/bin/bash
# Displays the size of the body of the response
curl -iLs '$1' | grep Content-Length | awk -F  "Content-Length: " '{print $2}'
