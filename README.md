# XSPFToolkit
* * *
This toolkit provides some scripts, which can be used to modify your playlists.

## xspfshuffler
It shuffles all the tracks it can find.

Before:  
```xml
<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/">
	<trackList>
		<track><location>file:///mp3s/song_1.mp3</location></track>
		<track><location>file:///mp3s/song_2.mp3</location></track>
		<track><location>file:///mp3s/song_3.mp3</location></track>
	</trackList>
</playlist>
```

After:  
```xml
<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/"><trackList><track><track><location>file:///mp3s/song_1.mp3</location></track>
<track><location>file:///mp3s/song_3.mp3</location></track>
<track><location>file:///mp3s/song_2.mp3</location></track></trackList></playlist>
```
(newlines and tabs stay removed.)

## xspfexeraser
It removes most of the tags of extensions like vlc  
*(Does not remove tabs. Intended to be run after xspfshuffler. This might change in the future... ;) )*

Before:  
```xml
<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/">
	<trackList>
		<track>
			<title>Sick H1P-H0P</title>
			<location>file:///mp3s/song_1.mp3</location>
			<extension application="http://www.videolan.org/vlc/playlist/0">
				<vlc:id>3</vlc:id>
				<vlc:option>start-time=42</vlc:option>
				<vlc:option>stop-time=45</vlc:option>
				<vlc:option>no-audio</vlc:option>
				<vlc:option>some-option=100</vlc:option>
			</extension>
		</track>
		<track>
			<title>Something else...</title>
			<location>file:///mp3s/song_2.mp3</location>
			<extension application="http://www.videolan.org/vlc/playlist/0">
				<vlc:id>4</vlc:id>
				<vlc:option>start-time=49</vlc:option>
				<vlc:option>stop-time=55</vlc:option>
			</extension>
		</track>
	</trackList>
</playlist>
```

After:  
```xml
<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/"><trackList><track><track><title>Something else...</title><location>file:///mp3s/song_2.mp3</location></track>
<track><title>Sick H1P-H0P</title><location>file:///mp3s/song_1.mp3</location></track></trackList></playlist> 
```

## xspfcreator
It creates a xspf-styled file out of a list of file paths.  
*(By default, it will change the contents of the given files. If you just want a command-line output, use: '--only-print' )*
Before:  
```
file:///song_1.mp3
file:///song_2.mp3
file:///song_3.mp3
```

After:  
```xml
<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/">
	<trackList>
		<track><location>file:///song_1.mp3</location></track>
		<track><location>file:///song_2.mp3</location></track>
		<track><location>file:///song_3.mp3</location></track>
	</trackList>
</playlist>
```

### Have fun