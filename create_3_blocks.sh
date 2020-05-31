#!/usr/bin/env bash

echo "$(chordmagician)$(chordmagician)$(chordmagician)" | abcm2ps - -O- | sed 's/\/r1{.*/\/r1{}!/' | ps2pdf - output.pdf
