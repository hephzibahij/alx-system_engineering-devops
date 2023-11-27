#!/usr/bin/env bash
# Puppet script to change client config file ssh

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication yes',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/id_rsa',
  match => '^#   IdentityFile ~/.ssh/id_rsa',
}

file { '/home/vagrant/.ssh/id_rsa':
  source  => '/vagrant/id_rsa',
  mode    => '0600',
  owner   => 'vagrant',
  group   => 'vagrant',
}

class { 'ssh':
  service_hasstatus => false,
  service_restart   => '/etc/init.d/ssh reload',
  service_name      => 'ssh',
}
