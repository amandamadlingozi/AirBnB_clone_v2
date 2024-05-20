# Ensuring Nginx is installed
package { 'nginx':
ensure => installed,
}

# Ensuring directories are created
file { '/data':
ensure => directory,
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/data/web_static':
ensure => directory,
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/data/web_static/releases':
ensure => directory,
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/data/web_static/shared':
ensure => directory,
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
ensure => directory,
owner  => 'ubuntu',
group  => 'ubuntu',
}

# Ensuring that a fake HTML file is created
file { '/data/web_static/releases/test/index.html':
ensure  => present,
content => '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>',
owner   => 'ubuntu',
group   => 'ubuntu',
}

# Ensuring that symbolic link is created
file { '/data/web_static/current':
ensure => link,
target => '/data/web_static/releases/test',
owner  => 'ubuntu',
group  => 'ubuntu',
}

# Restarting Nginx
service { 'nginx':
ensure    => running,
enable    => true,
subscribe => File['/data/web_static/current'],
}

# Updating Nginx configuration
file { '/etc/nginx/sites-available/default':
ensure  => present,
content => "
server {
listen 80 default_server;
listen [::]:80 default_server;

root /var/www/html;

index index.html index.htm index.nginx-debian.html;

server_name _;

location /hbnb_static {
alias /data/web_static/current;
}
}
",
notify  => Service['nginx'],
}

