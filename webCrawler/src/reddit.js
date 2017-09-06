import Nightmare from 'nightmare';

class RedditCrawler {
    constructor() {
        this.threads = [];
        this.comments = [];
    }

    async crawlSubreddit(redditUrl) {
        await this.crawlForThreads(redditUrl);
        await this.crawlThreads(redditUrl);
        return this.comments;
        // console.log(this);
    }

    async crawlForThreads(redditUrl) {
        const nightmare = new Nightmare({ show: false });
        // Go to initial start page, navigate to Detail search
        try {
            let self = this;
            await nightmare
                .goto(redditUrl)
                .evaluate(function () {
                    let links = [];
                    document.querySelectorAll('a.bylink').forEach((linkElement) => {
                        links.push(linkElement.href);
                    });
                    return {
                        links: links
                    }
                })
                .end()
                .then(function (result) {
                    self.threads = result.links;
                });
        } catch(e) {
            console.error(e);
        }
    }

    async crawlThreads() {
        let self = this;
        await Promise.all(this.threads.map(async (thread) => {
            await self.crawlThread(thread)
        }));
    }

    async crawlThread(redditThreadUrl) {
        const nightmare = new Nightmare({ show: false });
        let self = this;
        try {
            await nightmare
                .goto(redditThreadUrl)
                .evaluate(function () {
                    let comments = [];
                    document.querySelectorAll('.content .usertext-body').forEach((commentElement) => {
                        comments.push(commentElement.innerText);
                    });
                    return {
                        comments: comments
                    }
                })
                .end()
                .then(function (result) {
                    result.comments.forEach((comment) => {
                        self.comments.push(comment);
                    })
                });
        } catch(e) {
            console.error(e);
        }
    }
}

export default RedditCrawler;