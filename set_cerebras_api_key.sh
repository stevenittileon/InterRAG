#!/bin/bash
# Usage: source set_cerebras_api_key.sh
# This script will prompt you for your Cerebras API key and export it for the current shell session.

read -sp "Enter your Cerebras API key: " CEREBRAS_API_KEY
export CEREBRAS_API_KEY

echo -e "\nCEREBRAS_API_KEY has been set for this session." 