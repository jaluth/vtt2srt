# vtt2srt
Convert VTT subtitles (as used YouTube) to SRT format. 

## Requirements
Python 3.6+

## USAGE:

`python3 vtt2srt.py <input.vtt> <output.srt>`

### USAGE IN YOUR OWN PROJECTS

```
>>> import vtt2srt
>>> help(vtt2srt)

NAME
    vtt2srt - Convert .vtt subtitles to .srt format

FUNCTIONS
    main(input_file, output_file)
        Read VTT, convert, save to SRT

    read_vtt(filename)
        Read vtt into list

    vtt_to_srt(vtt)
        Convert VTT timestamps to SRT timestamps and insert SRT indeces

    write_srt(srt, filename)
        Write srt to disk

FILE
    vtt2srt/vtt2srt.py
```

