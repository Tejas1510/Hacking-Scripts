# Search Wikipedia using Voice
For searching queries on wikipedia using voice firstly we are using the `SpeechRecognition` library so that our device can recognize our voice command to take input and then `pyttsx3` library for converting text to speech so that the device can speak up the results or output, and last important library is `wikipedia` to access the article results for our queries. 

### SpeechRecognition

It is a library for performing speech recognition, with support for several engines and APIs, online and offline.

`SpeechRecognition` engine/API support:

- CMU Sphinx (works offline)
- Google Speech Recognition
- Google Cloud Speech API
- Microsoft Bing Voice Recognition
- Houndify API
- IBM Speech to Text

### pyttsx3 

`pyttsx3` is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

### wikipedia
`wikipedia` is a Python library that makes it easy to access and parse data from Wikipedia.

To search Wikipedia, get article summaries, get data like links and images from a page, and more. `wikipedia` wraps the MediaWiki API so you can focus on using Wikipedia data, not getting it.
