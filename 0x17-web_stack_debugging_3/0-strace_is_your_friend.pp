exec { 'fix-wordpress-permissions':
  command => 'chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html',
  onlyif  => 'test -d /var/www/html',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Exec['fix-wordpress-permissions'],
}
