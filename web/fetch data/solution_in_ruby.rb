require 'net/http'
require 'uri'
require 'json'
require 'open-uri'

datasource = 'https://www.reddit.com/r/subreddit.json'
uri = URI(datasource)
json = Net::HTTP.get(uri)
result = JSON(json)
puts result
