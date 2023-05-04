#!/usr/bin/env perl
 
use CGI qw{param};
 
print "Content-type: text/html\n\n";
 
sub login {
  $username = $_[0];
  $password = $_[1];
 
  $username =~ tr/a-z/A-Z/; # conver to uppercase
  $username =~ s/\s.*//;        # strip everything after a space
 
  @output = `egrep "^$username" /home/flag16/userdb.txt 2>&1`;
  foreach $line (@output) {
      ($usr, $pw) = split(/:/, $line);
 
      if($pw =~ $password) {
          return 1;
      }
  }
 
  return 0;
}
 
sub htmlz {
  print("Login resuls");
  if($_[0] == 1) {
      print("Your login was accepted");
  } else {
      print("Your login failed");
  }
  print("Would you like a cookie?
 
\n");
}
 
htmlz(login(param("username"), param("password")));
