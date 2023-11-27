#!/usr/bin/env bash
# Create or manage the SSH client configuration file

file { '/home/your_username/.ssh/config':
  ensure => file,
  owner  => 'your_username', # Replace with your actual username
  group  => 'your_username', # Replace with your actual username
  mode   => '0600',          # Set appropriate permissions

  content => "
    Host your_server
      HostName your_server_ip_or_hostname
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
