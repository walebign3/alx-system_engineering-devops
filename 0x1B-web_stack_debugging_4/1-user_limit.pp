# Change the open file limit for the current user
exec { 'increase performance':
  command => 'ulimit -n 5000'
  path    => '/bin:/usr/bin:/usr/sbin'
}
