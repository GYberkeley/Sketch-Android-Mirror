# Sketch-Android-Mirror
Allows you to mirror your Sketch Artboard to any Image Viewer on Android


In order to get to this work, you will need to install Sandbox.js to Sketch so that Sketch is allowed to access files outside of its own application folder. I specifically export the Artboard into a file onto the Desktop directory. If you're not comfortable with this, you can edit the directory that the file goes into by editing my sketch plugin file.

The Python listener uses Watchdog, which will listen for any pictures to land on whatever directory its snooping on. In this case, the artboard file will land on the Desktop that will then trigger an ADB push to the Android phone that you're currently using.

I'll make this simpler to use in due time but currently this is very modifiable so please fork it if you'd like.


