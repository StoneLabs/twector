# usage: __file__ <handle>
# returns: last 200 tweets of <handle> in JSON on STDOUT

require "net/http"
require "json"
require "oauth"
require "cgi"

ARGV[0] || abort("ERROR[#{__FILE__}]: NO HANDLE PROVIDED\nUSAGE: ruby #{__FILE__} <handle>")
handle = ARGV[0]
$auth = %x(source #{Dir.pwd}/auth.sh; echo $CONSUMER_KEY $CONSUMER_SECRET $API_KEY $API_SECRET).chomp.split

def oauth_get(_url)

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

followers = []
cursor = -1
begin
	$stderr.puts("cursor = #{cursor}")
	page = oauth_get("https://api.twitter.com/1.1/followers/list.json?cursor=#{cursor}&screen_name=#{CGI::escape(handle)}&count=200")
	followers.concat(page["users"])
	cursor = page["next_cursor"]
end while cursor != 0
$stderr.puts "Followers: #{followers.length}"

$stdout.puts followers.inspect
