# Increading worker_process from 1 to auto
exec { 'increase performance':
  command => "sed -i 's/worker_processes 1;/worker_processes auto;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
