getter-shell-version
-------
Exec getter in a more simple command with complement.

### Install:

	git clone https://github.com/code4craft/getter.git
	cd getter/shell
	ln -s `pwd`/add.sh /usr/local/bin/add
	ln -s `pwd`/edd.sh /usr/local/bin/edd
	
Add this line to /etc/bashrc(or ~/.profile, ~/.bashrc)

	export PATH=$PATH:/usr/local/getter
	
### Usage:

Only print text:
	
	add name value
	.name

Execute command:

	edd name value
	-name

Enjoy it!
