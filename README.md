# YouTubeChapterShortcuts
Native app required for the [YouTubeChapterShortcuts](https://addons.mozilla.org/en-US/firefox/addon/youtube-chapter-shortcuts/) Firefox extension. 

The shortcuts work even if Firefox and the YouTube tab is unfocused.

# Instructions
- Download this repository and unzip the contents to a folder.
- Run 'setup.bat'. (The path will be added to the registry and 'com.crambone.nativeapp.json' will be modified. **Don't move the files after you run setup.**) 
- (Optional) Customize the shortcuts in 'config.json'. (uses [pynput](https://pynput.readthedocs.io/en/latest/keyboard.html)).
- Add the YouTubeChapterShortcuts extension to Firefox.

**The default shortcuts are:**
- ctrl + (Comma): Previous chapter
- ctrl + (Period): Next chapter
- ctrl + (Semicolon): Switch the targeted tab

You can see which tab is targeted in the extension popup.
