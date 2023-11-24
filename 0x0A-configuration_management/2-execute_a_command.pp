# Puppet Manifest to Kill a Process Named "killmenow"

exec { 'kill-process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
