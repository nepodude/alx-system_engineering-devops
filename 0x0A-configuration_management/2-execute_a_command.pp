# This Puppet script kills any process named 'killmenow' using pkill

exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'pgrep -f killmenow',
}
