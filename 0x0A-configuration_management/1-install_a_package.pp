#!/usr/bin/env bash
# Puppet script that install flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
