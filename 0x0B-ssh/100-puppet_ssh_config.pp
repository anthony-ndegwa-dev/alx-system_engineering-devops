# Using puppet to change SSH config file
exec { 'echo':
  path    => 'usr/bin:/bin',
  command => 'IdentityFile ~/.ssh/school PasswordAuthentication no',
}
