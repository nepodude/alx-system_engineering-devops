# This manifest creates a file named 'school' in /tmp with specific permissions, ownership, and content.
file { '/tmp/school':
  ensure  => file,              # Ensures the file exists
  mode    => '0744',            # Sets file permissions to 0744 (rwxr--r--)
  owner   => 'www-data',        # Sets the file owner to 'www-data'
  group   => 'www-data',        # Sets the file group to 'www-data'
  content => 'I love Puppet',   # Sets the file content to 'I love Puppet'
}
