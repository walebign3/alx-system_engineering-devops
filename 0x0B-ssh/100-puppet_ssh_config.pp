# Update SSH configuration file
file_line { 'Update private key':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}

file_line { 'Update authentication method':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
