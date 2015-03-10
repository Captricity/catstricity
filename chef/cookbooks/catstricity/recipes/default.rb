#
# Cookbook Name:: catstricity
# Recipe:: default
#
# Copyright (c) 2015 The Authors, All Rights Reserved.

package 'git'

git '/mnt/chef-repo/application' do
  repository 'https://github.com/Captricity/catstricity.git'
  user 'ubuntu'
  group 'ubuntu'
end

# TODO: Install packages described in requirements.system
# TODO: Install python packages described in requirements.txt
# TODO: Run django commands migrate and initialize

package 'apache2'
package 'libapache2-mod-wsgi'

service 'apache2' do
  action [:start, :enable]
end

template '/etc/apache2/sites-enabled/django.conf' do
  source 'httpd.conf.erb'
end
