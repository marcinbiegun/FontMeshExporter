INKSCAPE_BIN="/Applications/Inkscape.app/Contents/Resources/bin/inkscape"
BLENDER_BIN="/Applications/blender.app/Contents/MacOS/blender"

pwd = `pwd`.strip
chars = File.open('chars.txt').read.split(//).map(&:strip).reject { |c| c.empty? }

def run_cmd(cmd)
  puts cmd
  system cmd
end

chars.each_with_index do |char, i|
  char_number = char.ord.to_s(16).upcase
  puts "\n\n\n\n#{i+1}/#{chars.count} - processing #{char} #{char_number}"

  svg_font_path = "#{pwd}/svg/Ux#{char_number}_font.svg"
  svg_path = "#{pwd}/svg/Ux#{char_number}.svg"
  obj_path = "#{pwd}/obj/Ux#{char_number}.obj"

  # Put char in SVG template
  svg_template = File.open('single_char_template.svg').read
  file = File.open(svg_font_path, 'w')
  file.write(svg_template.gsub(/\<\!\-\-CHAR\-\-\>.*\<\!\-\-CHAR\-\-\>/, char))
  #file.write("<svg><text>#{char}</text></svg>")
  file.close()

  # Inkscape: convert SVG to vectors
  run_cmd "#{INKSCAPE_BIN} -z -D --file=#{svg_font_path} --export-plain-svg=#{svg_path} --export-text-to-path"

  # Blender: convert SVG to OBJ
  run_cmd "#{BLENDER_BIN} -b -P blender_svg_to_obj.py -- --svg_import '#{svg_path}' --save '#{obj_path}'"
end
