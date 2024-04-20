#bin/user//bin/pup
# Installs a specific of flask  {2.1.0}
package { 'flask':
  ensure   => '2.5.0',
  provider => 'pip'
}
