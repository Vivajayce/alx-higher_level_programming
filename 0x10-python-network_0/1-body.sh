#!/bin/bash
# that takes in a URL, sends a request to that URL using curl, and displays the size of the body of the response in bytes
curl -sL "$1"
