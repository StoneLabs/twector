# usage: __file__ <handle>
# returns: last 200 tweets of <handle> in JSON on STDOUT

require "net/http"
require "json"
require "oauth"
require "cgi"
require "./lib.rb"
require "yaml"

ARGV[0] || abort("ERROR[#{__FILE__}]: NO HANDLE PROVIDED\nUSAGE: ruby #{__FILE__} <handle>")
handle = ARGV[0]
$auth = YAML.load open("#{Dir.pwd}/auth.yaml", &:read)

tweets = []

last_id = 0

10.times do
	res = Twector::oauth_get("https://api.twitter.com/1.1/statuses/user_timeline.json?" + {
		"screen_name" => handle,
		"count" => "2000"
	}.to_a.map{|i|[CGI::escape(i[0]),CGI::escape(i[1])].join(?=)}.join(?&))
	tweets += res
	last_id = res.map{|i|i["id"]}.max
end

$stdout.puts JSON.dump tweets
