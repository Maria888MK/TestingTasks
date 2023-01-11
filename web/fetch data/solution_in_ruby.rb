require 'net/http'
require 'uri'
require 'json'
require 'open-uri'

uri = URI('https://www.reddit.com/r/subreddit.json')
json = Net::HTTP.get(uri)
result = JSON(json)
puts result
