 use warnings;
 use strict;

print "What's your name:  ";
chomp(my $name = <STDIN>);
my $lnIndex = index($name, " ");
my $lastname = substr($name, $lnIndex + 1, length($name) - $lnIndex);
my $firstname = substr($name, 0, $lnIndex);

print "\nFirst Name: $firstname\n";
print " Last Name: $lastname\n";