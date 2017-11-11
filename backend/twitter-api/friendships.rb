require "twitter"

# usage: __file__ <handle>
# returns: all friendships of <handle> in JSON on STDOUT

%x(source #{Dir.pwd}/auth.sh; echo $CONSUMER_KEY $CONSUMER_SECRET $API_KEY $API_SECRET)
