import Nightmare from 'nightmare';
const nightmare = Nightmare({ show: true });
const norskReddit = 'https://www.reddit.com/r/norge/';


nightmare
    .goto(norskReddit)
    .end()
    .then(console.log);