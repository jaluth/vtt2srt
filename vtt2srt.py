#!/usr/bin/env python3
"""Convert .vtt subtitles to .srt format"""

import re
import sys

def read_vtt(filename):
    """Read vtt into list"""
    with open(filename, mode="rt", encoding="utf-8") as f:
        return [line for line in f]

def write_srt(srt, filename):
    """Write srt to disk"""
    with open(filename, mode="wt", encoding="utf-8") as f:
        f.writelines(srt)
        return

def vtt_to_srt(vtt):
    """Convert VTT timestamps to SRT timestamps and insert SRT indeces"""
    timestamp_find     = r'(\d\d:\d\d:\d\d).(\d\d\d) --> (\d\d:\d\d:\d\d).(\d\d\d)'
    timestamp_replace  = r'\1,\2 --> \3,\4'

    srt = []
    srt_index = 1
    for line in vtt:
        if re.search(timestamp_find, line):
            srt.append(f'{srt_index}\n') # Insert index
            srt_index += 1
            line = re.sub(timestamp_find, timestamp_replace, line) # Convert timestamp
        srt.append(f'{line}')

    return srt[4:] # Skip VTT header

def main(input_file, output_file):
    """Read VTT, convert, save to SRT"""
    vtt = read_vtt(input_file)
    srt = vtt_to_srt(vtt)
    write_srt(srt, output_file)
    return

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'USAGE: {sys.argv[0]} <input.vtt> <output.srt>')
    else:
        main(sys.argv[1], sys.argv[2])
        print('Done.')
