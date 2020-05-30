use strict;
use warnings;
use diagnostics;

sub program() {
    # actuall program to run
}



my ($username, $password) = ("admin", "admin1234");

print "Username:\n>";
chomp(my $usr = <STDIN>);
print "Password:\n>";
chomp(my $pswd = <STDIN>);

# compare the usernames and passwords
if ($usr eq $username && $pswd eq $password) {
    print "\nLogged in!\n";
    program();
} else { print "\nIncorrect!\n"; }