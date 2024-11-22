#!/bin/bash

url="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

response=$(curl -s "$url")

receipt_time=$(echo "$response" | jq -r '.[].receiptTime')

echo "$receipt_time" | head -n 6 
