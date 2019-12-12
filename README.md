# vobatching
This PYTHON 3 script does 3 things:

Read a .CSV document (from a sheet) with the VO file names, ID and comments. As well as audio files bounced from Pro Tools, specified on folder path depending on Character and Actor.
Rename such files depending on the ID specified on the CSV, identifying variations of the same line by ID and renaming accordingly.
Write a .txt that contains both the File Name and the Container name for each line and variations. Tab delimited.
The sound designer can then use that text file on Wwise with the “import Voice Assets” function and then import all the audio files and select Replace Existing.

Conclusion

I did a small survey on how long it took editors to deal with the VO files editing, renaming and during implementation and we can estimate that this script reduces such process by 50% of the time it would take with the current VFS method. 


It is important to point that this method may not work as well for all scenarios as this is focused on projects with MANY SHORT LINES WITH MANY VARIATIONS. And it would have diminishing returns if tried to apply to more linear dialogue. 



TO DO:

The current version doesn’t support adding the sheet (csv) comments to Wwise Files and is treated as unfinished/W.I.P., but that can be added with a few lines of code depending if the sound designers want to have that option.
This is a prototype for a ReaScript (Reaper) project that would potentially reduce the whole editing process to a matter of a hundred lines per hour. As well as further reducing the human error potential to zero during bouncing and implementation.
