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

## How it works

1. Builds a svg image with a single character in the center

2. Converts the svg image with a character into vectors using Inkscape 

```bash
/Applications/Inkscape.app/Contents/Resources/bin/inkscape -z -D --file=~Projects/font-to-obj/svg/Ux5D0_font.svg --export-plain-svg=/Users/n23/Projects/font-to-obj/svg/Ux5D0.svg --export-text-to-path
```

3. Uses Blender script to import the svg vector file, extrude the object and export it as an obj file

```bash
/Applications/blender.app/Contents/MacOS/blender -b -P blender_svg_to_obj.py -- --svg_import '~/Projects/font-to-obj/svg/Ux5D0.svg' --save '~/Projects/font-to-obj/obj/Ux5D0.obj'
```
