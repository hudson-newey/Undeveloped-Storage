require 'mail'  # ruby mail library. https://github.com/mikel/mail
 
puts "Sender username,"
$username = gets.chomp
puts ""
puts "Sender password,"
$password = gets.chomp
puts ""
puts "Sender domain,"
$domain = gets.chomp
puts ""
puts "Sender Adress,"
$address = gets.chomp
puts ""
puts "Email Message,"
$bodyMessage = gets
puts ""

system "cls"
puts "Receiver List,"
$reclist = gets.chomp

# configure delivery and retrieval methods
Mail.defaults do
  delivery_method :smtp, { 
                           :address              => $address,
                           :port                 => 587,
                           :domain               => $domain,
                           :user_name            => $username,
                           :password             => $password,
                           :authentication       => :login,
                            :enable_starttls_auto => true  
                           }
 
  retriever_method :pop3, { :address    => $address,
                          :port       => 995,
                          :user_name  => $username,
                          :password   => $password,
                          :enable_ssl => true    }
end
 
# send messages
puts "Sending to:"
Mail.deliver do
	f = File.open($reclist, "r")
	f.each_line do |line|
		puts line
		from    $address
		to      line
		subject 'IMPORTANT! PLEASE READ!'
		body    $bodyMessage
	end
	f.close
end