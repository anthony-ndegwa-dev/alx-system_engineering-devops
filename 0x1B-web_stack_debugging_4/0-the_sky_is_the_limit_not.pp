# Fix nginx high request problem

exec { 'upgrade':
  path    => '/bin/',
  command => 'sed -i "s/15/4096" /etc/default/nginx',
}

exec { 'restart':
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
