#!/bin/bash

set -xe

SAMPLE_FOLDER="${1:-/media/samples}"

find "${SAMPLE_FOLDER}" -name "*.mp3" -print0 |
    while IFS= read -r -d "" i; do
	ffmpeg -nostdin -i "${i}" -ac 1 "${i%.*}.wav"
	rm "${i}"
    done

find "${SAMPLE_FOLDER}" -name "*.wav" -exec  normalize-audio -v -b {} +

sync
