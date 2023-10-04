#!/usr/bin/env ruby
# A script that matches a regex expression

puts ARGV[0].scan(/^\d{10}$/).join
