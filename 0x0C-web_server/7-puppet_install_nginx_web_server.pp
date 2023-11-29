#!/usr/bin/env bash
#Puppet script to install nginx

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    content => template('nginx/default.erb'),
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
  }
}

# Redirect /redirect_me to / using 301 Moved Permanently
class redirect {
  exec { 'create redirect rule':
    command => '/bin/sed -i "s|location / {|location / {\n  return 301 /;\n}|" /etc/nginx/sites-available/default',
    notify  => Service['nginx'],
    require => File['/etc/nginx/sites-available/default'],
  }
}

# Main class
class { 'nginx': }
class { 'redirect': }
