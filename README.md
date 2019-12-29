# gbamp

Very simple music player for the Game Boy Advance. Currently supports only one file per ROM and lacks playback controls (only a stop button). It uses minimal battery power.

Audio is uncompressed PCM. Quality is fixed at 8-bit 32,768Hz stereo. This is (I think) the highest quality audio possible on the GBA, and it sounds better than you'd expect.

## TODO

- Playback controls
- Multiple tracks / bookmarks
- Support other frequencies, mono audio
- Album art

## Building

Use `make` to build. You will need devkitPro. The Makefile uses my ["inline alias"](https://github.com/vanjac/gas-inline-alias) preprocessor script for assembly files, which requires Python 3.

## Creating ROMs from audio files

The GBA plays 8-bit audio. Converting audio to 8-bit will produce artifacts for any music, but they will be especially noticeable for songs with a large dynamic range. Quiet sounds become fuzzy and distorted. Make sure your audio files are amplified as much as possible before converting them.

You will first need to convert your audio files to raw, *signed* 8-bit 32768Hz stereo PCM audio. You can use the `batchconvert.sh` script for this (requires ffmpeg). It will convert MP3 files in the current directory to `.raw` files. You can modify the script to search for different extensions.

Then run the `inline_alias.py` script in the same directory as your `.raw` files as well as `gbamp.gba`. This will produce a `.gba` ROM file for each audio file.

## Usage

Launch the ROM and the audio should start playing immediately. The screen is blanked to save power.

Press A+B+Start to stop the audio and exit. It will also exit automatically when the song is complete. If you run the ROM on a Visoly linker, EZ-FLASH cart, or Super Card, this will return to the main menu so you can select another ROM.
