from redmail import gmail
from YahooFinance import *
from Web_Scraping import *
from Update_Addresses import *
portfolio = ["SPY", "VTI", "QQQ", "BRK-B", "GOVT", "BND"]
stock_info = []
charts = []
newspaper = []

for i in portfolio:
    chart = make_chart(i, portfolio.index(i) + 1)
    charts.append(chart[0])
    stock_info.append(chart[1])
    news = get_news(i)
    newspaper.append(news)
    time.sleep(0.5)

front_page = get_articles('https://www.wsj.com/')
articles = front_page[0]
links = front_page[1]
time.sleep(0.5)
economic_page = get_articles('https://www.wsj.com/news/economy')
e_articles = economic_page[0]
e_links = economic_page[1]
time.sleep(0.5)
v_news = villanovan()

v_articles = v_news[0]
v_links = v_news[1]
# Colors
#329ea8
#88e2eb

html_message = """
<html>
<style>
a:link, a:visited {
    color: black;
}


.image {
    float: left;
    width: 68%;
    border: none;
    height: none;
    margin: 1%;
}

.title {
    font-size: 5vmin;
    padding: 1vmin;
    padding-bottom: 0px;
    text-align: left;

}

.norm {
    clear: left;
    width: 90%;
    background-color: #d1e2ff;
    margin: 5%;
    text-align: center;
}

body {
    background-color: #4071c2;
}

img {
    max-width: 100%
    max-height: 100%;
}
.stock_chart{
    max-width: 40%;
    margin-bottom: 5%;
    float: left;
    margin-left: 5%;
    margin-right: 5%;
    word-wrap: break-word;
}

#left {
    clear: left;
}

.article {
    background-color: lightgray;
    margin-bottom: 5%;
    float: left;
    margin-left: 5%;
    margin-right: 5%;
    word-wrap: break-word;
    padding-top: 1%;
    padding-bottom: 1%;
    width: 40%
}

.foot {
    text-align: center;
    font-weight: bold;
    padding: 5%;
    background-color: lightgray;
}

h3 {
    text-decoration: none;
}

</style>

<div class="norm">
    <a href="https://forms.gle/aDr8JVTjr2em6zMc8">
        <div style="padding: 5%; ">{{ Courier }}</div>
    </a>
</div>
<div class="norm">
    <h1 style="padding-top: 5%;"> Last 24 hours of Stock Movement </h1>
    <div class="stock_chart">
        {{ img_1 }}
        <h3> {{ info_1 }} </h3>
        <p><a href="{{link_1}}"> {{ new_1 }} </a></p>
    </div>
    <div class="stock_chart">
        {{ img_2 }}
        <h3> {{ info_2 }} </h3>
        <p><a href="{{link_2}}"> {{ new_2 }} </a></p>
    </div>
    <div class="stock_chart" id='left'>
        {{ img_3 }}
        <h3> {{ info_3 }} </h3>
        <p><a href="{{link_3}}"> {{ new_3 }} </a></p>
    </div>
    <div class="stock_chart">
        {{ img_4 }}
        <h3> {{ info_4 }} </h3>
        <p><a href="{{link_4}}"> {{ new_4 }} </a></p>
    </div>
    <div class="stock_chart" id='left'>
        {{ img_5 }}
        <h3> {{ info_5 }} </h3>
        <p><a href="{{link_5}}"> {{ new_5 }} </a></p>
    </div>
    <div class="stock_chart">
        {{ img_6 }}
        <h3> {{ info_6 }} </h3>
        <p><a href="{{link_6}}"> {{ new_6 }} </a></p>
    </div>
    <p style="clear: left; padding-bottom: 5%;"> Created using yahoo finance api data compiled into matplotlib charts</p>
</div>

<div class='norm'>
    <h1 style="padding-top: 5%;">Wall Street Journal</h1>
    <h2> Front Page </h3>
    <div class='article' id='left'>
        <h3><a href="{{ wsj_link_0 }}"> {{ title_0 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ wsj_link_1 }}"> {{ title_1 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ wsj_link_2 }}"> {{ title_2 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ wsj_link_3 }}"> {{ title_3 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ wsj_link_4 }}"> {{ title_4 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ wsj_link_5 }}"> {{ title_5 }} </a></h3>
    </div>
    <center>
    <h2 style="clear: left;"> Economic News </h2>
    </center>
    <div class='article' id='left'>
        <h3><a href="{{ e_link_0 }}"> {{ e_title_0 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ e_link_1 }}"> {{ e_title_1 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ e_link_2 }}"> {{ e_title_2 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ e_link_3 }}"> {{ e_title_3 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ e_link_4 }}"> {{ e_title_4 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ e_link_5 }}"> {{ e_title_5 }} </a></h3>
    </div>
    <br>
    <h1 id='left'>-</h1>
</div>
<div class='norm'>
    <h1 style="padding-top: 5%"> Villanova News </h1>
    <div class='article' id='left'>
        <h3><a href="{{ v_link_0 }}"> {{ v_title_0 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ v_link_1 }}"> {{ v_title_1 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ v_link_2 }}"> {{ v_title_2 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ v_link_3 }}"> {{ v_title_3 }} </a></h3>
    </div>
    <div class='article' id='left'>
        <h3><a href="{{ v_link_4 }}"> {{ v_title_4 }} </a></h3>
    </div>
    <div class='article'>
        <h3><a href="{{ v_link_5 }}"> {{ v_title_5 }} </a></h3>
    </div>
    <br>
    <h1 id='left'>-</h1>  
</div>
<div class='foot'>
    <h7> Built and Managed by Ryan Clothier</h7>
    <p>VSB '26</p>
    <a href = "www.linkedin.com/in/ryanclothier">
        <img src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAaVBMVEUAdrL///8Ab68Ac7AAca+DsNHt9PlQlcIAbK0AeLP7/v7K3uwIfLUAaawAa60Abq7E2Oiyz+JloMjb6fJ6q86bv9qKtdQ9i71tpMqpx97f6fLm8PZYmMQjgbgzh7uSudbR4+5Djr8AY6kYzK97AAADzUlEQVR4nO3bW3eqMBCGYSERIyLiWWs9dP//H7l12UqtmelpMilZ33PVC13lXeEQIPZ6AAAAAAAAAAAAAAAAAAAAAAAAAAAAQmzuXO0m1sTekDCMG262zfxpNO0faht7a+SZejDKbnb9PLVGW73ruyie69jbJMrNsgfTceytEuQWj4FZ1qQzitYzgkklmr0/MMtWk9jbJsPNqcJsn8SVkdpH09lPa3oI0xhEc2ACs2Uee/t+zx65wrmLvX2/50ZcYZbA5M3t2MJ19w9EW7CFs+4Poi3Zwk33C3N+DJ+7v5e6J7YwgQviZMoFlglcLaz3zunNKYHC3pAr7Hf/RHM+EBtmJ429cSLMmi5cpnGD6LZUYJHCUXhBXhIHKRyFF6byz2sWaeyjF/bgS+ynE3h5IPxwo1/OUjkIr4xb3R+MU5vKMXhj88XpLW+33Kc1gK+sy18Wx2X/eejy7s+3CcbaPNW3hwAA8HeZdK89Nnd1r9rv99XQ5LVL7TJra7PZjorrHUtZFrvRdnEYu2hT3SHpR580dbU6ZY/KZmMnUUbS7kpCNrjfINvPiA82t3vJ+6VHHyO3exehkXmu/1hIaN7uRdzaN3zvPxnhtkWw0FjyqVZrWWsPo1zhZM2/5nk1HyqfcsQK/UurPMoX3USpwnr1xcAz3UShQveNwKxUfWsnU5gzC488Cs1BFCms2WU53m90rPAfv6TDQ3ENhETh9DsH4VWht9xKovCJX9Hhpff2VaLwJ0q1ZdaxCrOF1iBGKzxpnU6jFaot1olXuFLaTeMVau2m8Qq1Vq9GLFRaFxigsJjPi6/MAZSWkcsWls3iYOuzcTWbflbZ6CyGEC08Wnd79nv+85PHNkpLkgQL59WHQXED/gsPT2T/eGHz+BTNMqvmzg4qpxqxQu/lLd9wX9FZRi5VWPrfM425R8Q6sxqpwr7/1G9emO9sVS4XQoXkeXHM/HRM53IhVHikhsMyTzhGKpcLoULyVoj+jarWSnmZwh39TGJC/4Odyt2FTOGWPqIcfTYtOlTIPHSZ0HO3skOFzOyEO9WoPG+TKWT+gWWmNd0ZQ+4JtnmmC7tzxedOityspjszb+7Cxv0qJ3DblUjhiJl+cT+ID9x2JVLYcGPITGoCt12hsPXDvbRXJVHITaFRGBoKWyikoDA0FLZQSEFhaChsoZCCwtBQ2EIhBYWhobCFQgoKQ0NhC4UUFIaGwhYKKSgMDYUtFFJQGBoKWyikoDA0FLZQSIld2DOkj5+0Ywq/5v7r/wEAAAAAAAAAAAAAAAAAAAAAAAAAAADu/Qc1IEgIC3Rq1AAAAABJRU5ErkJggg==" height="100" width="100">
    </a>
    <span style="font-weight:normal"><p> Unsubscribe <a href='https://forms.gle/hcCTsXpGbyzresd1A'> here </a></p></span>
</div>

</body>
</html>
"""

gmail.username = 'ryan.clothier123@gmail.com'
gmail.password = open("SMTP_Gmail.txt", "r").read()
gmail.send(
    subject="Update: The Clothier Courier!",
    bcc=get_emails(),
    html=html_message,
    body_images={"img_1": charts[0], "Courier": "Clothier Courier.jpg", "img_2": charts[1],
                 "img_3": charts[2], "img_4": charts[3], "img_5": charts[4], "img_6": charts[5]},
    body_params={"new_1": newspaper[0]['title'], "link_1": newspaper[0]['link'],
                 "new_2": newspaper[1]['title'], "link_2": newspaper[1]['link'],
                 "new_3": newspaper[2]['title'], "link_3": newspaper[2]['link'],
                 "new_4": newspaper[3]['title'], "link_4": newspaper[3]['link'],
                 "new_5": newspaper[4]['title'], "link_5": newspaper[4]['link'],
                 "new_6": newspaper[5]['title'], "link_6": newspaper[5]['link'],
                 "title_0": articles[0], "wsj_link_0": links[0],
                 "title_1": articles[1], "wsj_link_1": links[1],
                 "title_2": articles[2], "wsj_link_2": links[2],
                 "title_3": articles[3], "wsj_link_3": links[3],
                 "title_4": articles[4], "wsj_link_4": links[4],
                 "title_5": articles[5], "wsj_link_5": links[5],
                 "e_title_0": e_articles[0], "e_link_0": e_links[0],
                 "e_title_1": e_articles[1], "e_link_1": e_links[1],
                 "e_title_2": e_articles[2], "e_link_2": e_links[2],
                 "e_title_3": e_articles[3], "e_link_3": e_links[3],
                 "e_title_4": e_articles[4], "e_link_4": e_links[4],
                 "e_title_5": e_articles[5], "e_link_5": e_links[5],
                 "v_title_0": v_articles[0], "v_link_0": v_links[0],
                 "v_title_1": v_articles[1], "v_link_1": v_links[1],
                 "v_title_2": v_articles[2], "v_link_2": v_links[2],
                 "v_title_3": v_articles[3], "v_link_3": v_links[3],
                 "v_title_4": v_articles[4], "v_link_4": v_links[4],
                 "v_title_5": v_articles[5], "v_link_5": v_links[5],
                 "info_1": stock_info[0], "info_2": stock_info[1],
                 "info_3": stock_info[2], "info_4": stock_info[3],
                 "info_5": stock_info[4], "info_6": stock_info[5]
                 }
)
