# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
execute 'apt_update' do
  command 'apt-get update'
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
package "ack-grep"
cookbook_file "ntp.conf" do
  path "/etc/ntp.conf"
end
execute 'ntp_restart' do
  command 'service ntp restart'
end
execute 'install_pip' do
  command 'wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py'
end
execute 'install_django' do
  command 'pip install django'
end
execute 'install_eyed3' do
  command 'pip install eyeD3'
end
execute 'runserver' do
  cwd '/home/vagrant/project/mysite'
  command 'nohup python manage.py runserver 0.0.0.0:8080 &'
  user 'vagrant'
end
