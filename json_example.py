import re

json_example =  {
    "status": "ok",
    "totalResults": 10,
    "articles": [
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Flight diverted after passenger finds live mouse in meal",
    "description": "The furry stowaway forced a Scandinavian Airlines plane to make an emergency landing.",
    "url": "https://www.bbc.co.uk/news/articles/ckgmy2d09x2o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/d6e4/live/056409f0-7761-11ef-861f-71b4ea79cd37.jpg",
    "publishedAt": "2024-09-20T16:22:19.7627384Z",
    "content": "Airlines usually have strict restrictions involving rodents on board planes in order to prevent electrical wiring being chewed through.\r\n\"Believe it or not. A lady next to me here at SAS opened the f… [+676 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Mark Robinson: North Carolina governor candidate denies 'black Nazi' post",
    "description": "Mark Robinson insists he will stay in the governor race in the swing state.",
    "url": "https://www.bbc.co.uk/news/articles/c5yjgqxl00xo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/2f07/live/2ede91a0-76ae-11ef-bc61-1d45017a238a.jpg",
    "publishedAt": "2024-09-20T16:07:15.4944524Z",
    "content": "Robinson, 56, is a former furniture manufacturer who was elected to be the state's first black lieutenant governor in 2020.\r\nHe won the nomination to run for governor in March after receiving an endo… [+2603 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Myanmar's civil war threatens key China trade route",
    "description": "The BBC visits the border with Myanmar, where a war is raging on China’s doorstep.",
    "url": "https://www.bbc.co.uk/news/articles/czjyj2rd1zpo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/3c6a/live/d84c53b0-7665-11ef-8c1a-df523ba43a9a.jpg",
    "publishedAt": "2024-09-20T15:52:17.0903678Z",
    "content": "There is nothing for us to do in Myanmar because of the war, Zin Aung says. Everything is expensive. Rice, cooking oil. Intensive fighting is going on everywhere. Everyone has to run.\r\nHis parents ar… [+1155 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "US election polls tracker 2024: Who is ahead - Harris or Trump?",
    "description": "An in-depth look at the polls and what they can and can’t tell us about who will win the White House.",
    "url": "https://www.bbc.co.uk/news/articles/cj4x71znwxdo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/e457/live/d48d2d60-6f55-11ef-8c1a-df523ba43a9a.png",
    "publishedAt": "2024-09-20T15:37:18.4016614Z",
    "content": "The figures we have used in the graphics above are averages created by polling analysis website 538, external, which is part of American news network ABC News. To create them, 538 collect the data fr… [+430 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Israel investigates after its soldiers filmed throwing bodies off roof",
    "description": "The IDF says the incident does not \"conform\" to its values, while Palestinian officials say it is a \"crime\".",
    "url": "https://www.bbc.co.uk/news/articles/cn8jg0x5xg8o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/a6e6/live/46c0e6a0-7754-11ef-b02d-c5f3b724a1ea.jpg",
    "publishedAt": "2024-09-20T15:22:13.2168974Z",
    "content": "Under international law, soldiers are obliged to ensure that bodies, including those of enemy fighters, are treated with respect. \r\nThe IDF said it carried out a counterterrorism operation in Qabatiy… [+1823 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Pakistani blasphemy: Suspect dead in alleged shootout with police",
    "description": "Dr Shah Nawaz is the second blasphemy suspect to be shot dead by police in the space of a week.",
    "url": "https://www.bbc.co.uk/news/articles/cz9pg8d4245o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/c80d/live/ac580150-7737-11ef-8fc1-d5cebdd30c6b.png",
    "publishedAt": "2024-09-20T12:22:21.2292662Z",
    "content": "According to a police report, officers in the city of Mirpur Khas had tried to stop two men riding on a motorcycle on Wednesday, in order to search their vehicle.\r\nInstead of complying, the report sa… [+1243 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Harris says anyone breaking into her home is 'getting shot'",
    "description": "The Democratic presidential nominee has discussed her gun ownership in a jokey exchange with Oprah Winfrey.",
    "url": "https://www.bbc.co.uk/news/articles/cn4yxe2xxzdo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/b65b/live/25f33cf0-7733-11ef-8c1a-df523ba43a9a.jpg",
    "publishedAt": "2024-09-20T10:37:19.1051532Z",
    "content": "Harris's gun ownership has been a matter of public record since 2019, when she said: I own a gun for probably the reason a lot of people do for personal safety. I was a career prosecutor.\r\nBut her ow… [+1423 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Hezbollah device explosions: The unanswered questions",
    "description": "The sabotage of thousands of pagers and walkie-talkies has raised many who, what and whys.",
    "url": "https://www.bbc.co.uk/news/articles/c0e1wpr0q44o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/5adf/live/168e1730-7729-11ef-b282-4535eb84fe4b.jpg",
    "publishedAt": "2024-09-20T09:22:16.6527219Z",
    "content": "The BBC went to the registered office of BAC Consulting, situated in a residential area of the Hungarian capital, Budapest.\r\nThe address appeared to be shared by 12 other companies - and no-one in th… [+1620 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "Russia’s war dead tops 70,000 as volunteers face 'meat grinder'",
    "description": "More than 70,000 Russian soldiers have died in Ukraine - volunteers now make up the highest number of deaths.",
    "url": "https://www.bbc.co.uk/news/articles/cjr3255gpjgo",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/5921/live/a421a040-76b5-11ef-b282-4535eb84fe4b.jpg",
    "publishedAt": "2024-09-19T23:52:15.6500089Z",
    "content": "A small number of the volunteers killed have been from other countries. We have identified the names of 272 such men, many of whom were from Central Asia - 47 from Uzbekistan, 51 from Tajikistan, and… [+1973 chars]"
    },
    {
    "source": {
    "id": "bbc-news",
    "name": "BBC News"
    },
    "author": "BBC News",
    "title": "French dig team gets 200-year-old note from archaeologist",
    "description": "A team of volunteer archaeologists in Normandy has had a surprise communication from the past.",
    "url": "https://www.bbc.co.uk/news/articles/c5yj7kg3zd1o",
    "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/b7f7/live/6ea1f120-7676-11ef-b1c4-496bb3338395.jpg",
    "publishedAt": "2024-09-19T14:22:22.0320779Z",
    "content": "On Tuesday evening, Mr Blondel opened the paper which read as follows:\r\nP.J Féret, a native of Dieppe, member of various intellectual societies, carried out excavations here in January 1825. He conti… [+611 chars]"
    }
    ]
    }



