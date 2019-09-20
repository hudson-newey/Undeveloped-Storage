#!/usr/local/bin/perl

use strict;
use warnings;
use LWP::UserAgent;

my $ua = new LWP::UserAgent;
$ua->timeout(120);
print "Website to Access\n:";
chomp(my $url = <STDIN>);
my $request = new HTTP::Request('GET', $url);
my $response = $ua->request($request);
my $content = $response->content();

open(my $fh, '>', 'website.html');
print $fh "$content\n";
close $fh;
