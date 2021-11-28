import csv
import tweepy

def main():

    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAMgCWQEAAAAAhD5zT%2F0CSz5%2FvBFYw6ONa8zhtEY%3DLuIyhyXTaPWIzJzRzRz6TIv1Jhq9uNYRY1km6X8hDHTSLO5faI')

    query = '(vaccine (covid OR covid19 OR pfizer OR moderna) OR coronavirus OR covid OR covid19 OR quarantine OR pandemic OR pfizer OR moderna) lang:en -is:retweet'

    tweets = client.search_recent_tweets(query=query, max_results=10)
    # print(tweets)

    output_file = '../data/filtered_tweets.tsv'

    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer=csv.writer(file, delimiter='\t')
        for tweet in tweets.data:
            writer.writerow([tweet.id, tweet.text.replace('\n',' ').replace('\t', ' ')])

if __name__ == '__main__':
    main()