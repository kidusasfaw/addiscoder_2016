# expand out the test cases inside the YML files to
#  individual .in and .out files
require 'yaml'

raise "no file" if ARGV.size < 1

# secret cases only flag
only_secret = false
ARGV.each do |arg|
  only_secret = true if arg == '-s'
end

s = IO.read ARGV[0]
y = YAML.load s

# old way that also writes out sample cases
=begin
y.size.times do |i|
  puts "Writing #{i}.in and #{i}.out"
  IO.write "#{i}.in", y[i]['input']
  IO.write "#{i}.out", y[i]['output']
end
=end

i = 1
y.each do |test|
  if !only_secret || test['is_secret']
    puts "Writing #{i}.in and #{i}.out"
    IO.write "#{i}.in", test['input']
    IO.write "#{i}.out", test['output']
    i+=1
  end
end
