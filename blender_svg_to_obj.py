import argparse
import bpy

SVG_OBJECT_NAME = "path10"

def get_args():
  parser = argparse.ArgumentParser()

  # get all script args
  _, all_arguments = parser.parse_known_args()
  double_dash_index = all_arguments.index('--')
  script_args = all_arguments[double_dash_index + 1: ]

  # add parser rules
  parser.add_argument('-n', '--svg_import', help="path to SVG file")
  parser.add_argument('-m', '--save', help="output file")
  parsed_script_args, _ = parser.parse_known_args(script_args)
  return parsed_script_args

args = get_args()
file_loc = args.svg_import

# Delte default objects
bpy.data.objects['Cube'].select_set(True)
bpy.data.objects['Light'].select_set(True)
bpy.data.objects['Camera'].select_set(True)

bpy.ops.object.delete()

# Import svg
bpy.ops.import_curve.svg(filepath=file_loc)

# Resize to fill [1, 1, 1]
bpy.data.objects[SVG_OBJECT_NAME].dimensions = [1, 1, 1]

# Select it
bpy.data.objects[SVG_OBJECT_NAME].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects[SVG_OBJECT_NAME]

# Move to origin
bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

# Apply solidify
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.05

# Export OBJ
bpy.ops.export_scene.obj(filepath=args.save)

