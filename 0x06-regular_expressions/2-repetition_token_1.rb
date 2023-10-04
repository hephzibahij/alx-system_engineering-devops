#!/usr/bin/env bash
# Script that matches to a regex pattern

puts ARGV[0].scan(/hb?tn/).join
