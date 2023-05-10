# Use strace to find & fix why Apache returns 500 error, then automate using Puppet

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settingls.php'
}
