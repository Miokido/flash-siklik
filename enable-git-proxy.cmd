@echo off
echo This script is used on machines where proxy configuration is boring.

set /p "c3user=c3 username : "
set /p "c3password=c3 password : "

git config --global http.proxy http://%c3user%:%c3password%@proxy.server.com:port