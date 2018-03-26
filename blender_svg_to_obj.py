import argparse
import bpy

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
bpy.data.objects['Cube'].select = True
bpy.data.objects['Lamp'].select = True
bpy.data.objects['Camera'].select = True
bpy.ops.object.delete()

# Import svg
bpy.ops.import_curve.svg(filepath=file_loc)

# Resize to fill [1, 1, 1]
bpy.data.objects["Curve"].dimensions = [1, 1, 1]

# Select it
bpy.data.objects["Curve"].select = True
bpy.context.scene.objects.active= bpy.data.objects["Curve"]

# Move to origin
bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

# Apply solidify
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.05

# Export OBJ
bpy.ops.export_scene.obj(filepath=args.save)

