# frozen_string_literal: true

# import required modules
require 'net/http'
require 'uri'
require 'json'
require 'open-uri'

loop do
  # source URL to fetch the data
  uri = URI('https://www.reddit.com/r/subreddit.json')

  # put your webhook url here
  webhook_url = 'https://webhook.site/387a6309-3688-4457-b4f1-193ea702bc24'

  json = Net::HTTP.get(uri)
  data_hash = JSON.parse(json)

  # create hash object
  extracted_data = {}

  # fill in the hash object using the extracted json data( title, url)
  data_hash['data']['children'].each do |child|
    title = child['data']['title']
    url_from_json = child['data']['url']
    extracted_data[title] = url_from_json
  end

  # REVIEW: the hash object in the console
  extracted_data_json_format = JSON.pretty_generate(extracted_data)
  puts extracted_data_json_format

  # push data to webhook.site
  webhook_uri = URI(webhook_url)
  res = Net::HTTP.post_form(webhook_uri, extracted_data)
  puts res.body if res.is_a?(Net::HTTPSuccess)
  
  # repeat the entire script each minute
  sleep 60
end
