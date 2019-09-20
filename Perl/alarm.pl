use strict;
# get user input
print("Time to wait:\n");
my $wait = <STDIN>;
chomp($wait); # remove newline

for (my $i = 0; $i < $wait; $i++) {
    cls(); # call clear screen function
    print($wait - $i, "\n");
    sleep(1);
}

sub cls {
    print "\033[2J";    #clear the screen
    print "\033[0;0H"; #jump to 0,0
}