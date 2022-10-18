# Client configuration using puppet
file { '/etc/ssh/ssh_config':
content => "PasswordAuthentication no \n IdentityFile ~/.ssh/school"
}
