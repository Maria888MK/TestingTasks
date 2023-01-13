require 'net/http'
require 'uri'
require 'json'
require 'open-uri'

while true
  # Create the HTTP objects
  uri = URI('https://www.reddit.com/r/subreddit.json')
  webhook_url = 'https://webhook.site/387a6309-3688-4457-b4f1-193ea702bc24'
  json = Net::HTTP.get(uri)


  # puts elements
  data_hash = JSON.parse(json)
  # elements = data_hash['data']['dist']
  extracted_data = {}


  data_hash['data']['children'].each do |child|
    title = child['data']['title']
    url_from_json = child['data']['url']
    extracted_data[title] = url_from_json
  end
  extracted_data_json_format = JSON.pretty_generate(extracted_data)
  puts extracted_data_json_format
  # Post the data to endpoint server
  webhook_uri = URI(webhook_url)
  res = Net::HTTP.post_form(webhook_uri, extracted_data)
  puts res.body  if res.is_a?(Net::HTTPSuccess)
  # encoded_params = URI.encode_www_form(extracted_data)
  # response = Faraday.post(webhook_url, encoded_params)
  # p response.body if response.status == 201
  sleep 60
end
