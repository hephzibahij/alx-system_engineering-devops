#!/usr/bin/env bash
# Puppet that install flask

package { 'flask':
  ensure   => '2.0.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
