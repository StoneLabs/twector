module Twector
	def self.oauth_get(_url)
		url = URI(_url)
		http = Net::HTTP.new(url.host, url.port)
		http.use_ssl = true
		http.verify_mode = OpenSSL::SSL::VERIFY_PEER
		request = Net::HTTP::Get.new(url.request_uri)
		request.oauth!( http, OAuth::Consumer.new($auth[0], $auth[1]), OAuth::Token.new($auth[2], $auth[3]) )
		response = nil ; http.start{response=http.request(request)}
		raise("HTTP Error #{response.code}") if response.code[0]!='2'
		return JSON.parse response.body
	end
end
