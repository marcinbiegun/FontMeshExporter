# font-to-obj

A script for Batch conversion of single font characters to extruded OBJ models.

It works fine with all kinds of unholy Unicode symbols.

![font-to-obj](https://raw.githubusercontent.com/marcinbiegun/font-to-obj/master/docs/font-to-obj.png)

## Dependencies

* Inkscape for creating vectors from fonts
* Blender for creating 3d models from vectors

## How to run it

Tested on MacOS.

1. Install Inkscape and Blender, put .app files inside `/Applications` directory.
2. Write your characters inside `chars.txt` file.
3. Run `ruby run.rb`.
4. Receive OBJs in `obj` directory.

