module Twector
	def self.oauth_get(_url)
		url = URI(_url)
		http = Net::HTTP.new(url.host, url.port)
		http.use_ssl = true
		http.verify_mode = OpenSSL::SSL::VERIFY_PEER
		request = Net::HTTP::Get.new(url.request_uri)
		request.oauth!( http, OAuth::Consumer.new($auth["CONSUMER_KEY"], $auth["CONSUMER_SECRET"]), OAuth::Token.new($auth["API_KEY"], $auth["API_SECRET"]) )
		response = nil ; http.start{response=http.request(request)}
		raise("HTTP Error #{response.code}") if response.code[0]!='2'
		return JSON.parse response.body
	end
end
