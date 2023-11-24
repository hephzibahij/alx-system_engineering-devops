# Using Puppet that install flask from pip3

package { 'flask':
  ensure   => '2.0.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
