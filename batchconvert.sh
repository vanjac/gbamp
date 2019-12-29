for i in *.mp3; do ffmpeg -i "$i" -f s8 -acodec pcm_s8 -ar 32768 "${i%.*}.raw"; done
