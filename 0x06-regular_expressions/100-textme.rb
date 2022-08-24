#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)(\+?[a-zA-Z0-9]+)|(?<=to:)(\+?[0-9a-zA-Z]+)|(?<=flags:)(-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1]:-?[0-1])/).join
