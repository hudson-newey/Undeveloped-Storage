use strict;
use warnings;

sub append {
	open(FH, '>>', "names.txt") or die $!;
	print FH "$_[0]\n";
	close(FH);
}

for (;;) {
	chomp(my $input = <STDIN>);
	append($input);
}