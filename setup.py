from fabric.api import *

env.user     = 'username'
env.password = 'password'
env.hosts    = ['host']

def set_up():
	sudo('yum -y remove postfix')
        sudo('yum -y remove cronie-anacron')
        sudo('yum -y groupinstall "X Window System" "Desktop" "Japanese Support" "development tools"')
	sudo('yum -y install logwatch jwhois cronie-noanacron sendmail sysstat ncurses-devel gcc-c++ readline-devel ncurses-devel zlib-devel openssl-devel flex libxml2-devel zlib-devel libpng-devel libjpeg-devel curl-devel libmcrypt-devel libmcrypt cmake swatch clamd pcre-devel ld-linux.so.2 libstdc++.so.6 libcap-devel libcap freetype-devel make libssh2-devel amavisd-new db4-devel libc-client libc-client-devel aspell aspell-devel krb5-libs krb5-workstation krb5-auth-dialog krb5-devel libc-client libc-client-devel cyrus-sasl cyrus-sasl-devel cyrus-sasl-md5 cyrus-sasl-plain cyrus-imapd cyrus-imapd-devel cyrus-imapd-utils sqlite sqlite-devel ImageMagick-c++-devel neon-devel perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker perl-devel perl-ExtUtils-Embed libyaml-devel lua-devel glib2-devel libevent-devel libcap compat-libcap1')
	sudo('yum -y install yum-priorities')
	sudo('yum -y update')
