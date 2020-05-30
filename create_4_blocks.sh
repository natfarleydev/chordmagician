#!/usr/bin/env bash

echo "$(python main.py)\n\n$(python main.py)\n\n$(python main.py)\n\n$(python main.py)" | abcm2ps - -O- | ps2pdf - output.pdf
