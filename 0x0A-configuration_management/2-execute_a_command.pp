# Kill a process
exec { 'kill process':
path    => '/usr/bin/',
command => 'pkill killmenow'
}
