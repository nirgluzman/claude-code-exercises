#!/bin/bash
model=$(cat | grep -o '"display_name":"[^"]*"' | head -1 | cut -d'"' -f4)
echo -e "\033[38;5;214m${model}\033[0m"
