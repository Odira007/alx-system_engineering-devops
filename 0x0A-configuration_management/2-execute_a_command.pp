# Execute a command using puppet
exec {'killmenow':
  command  => ['pkill'],
}
