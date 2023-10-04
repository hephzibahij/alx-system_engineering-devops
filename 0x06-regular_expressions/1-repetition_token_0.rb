#!/usr/bin/env ruby
# A script that matches a regular expression

puts ARGV[0].scan(/hbt{2,5}n/).join
