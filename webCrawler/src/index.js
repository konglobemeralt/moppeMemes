'use strict'
var fs = require('fs');
import RedditCrawler from './reddit';
const norskReddit = 'https://www.reddit.com/r/norge/';



const crawlReddit = async redditUrl => {
    let redditCrawler = new RedditCrawler();
    let comments = await redditCrawler.crawlSubreddit(redditUrl);
    fs.writeFile('../users.json', JSON.stringify(comments), 'utf-8', function(err) {
        if (err) throw err
        console.log('Done!')
    })
};
crawlReddit(norskReddit);

// getThreads(norskReddit);


