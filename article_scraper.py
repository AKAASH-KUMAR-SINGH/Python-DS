from database import Article,create_engine
from sqlalchemy.orm import 


def get_soup():
    url='http://blog.jetbrains.com'
    try:
        page=request.get(url)
        if

        


def extract(soup):
    terget=soup.find('div',class_='latest')
    if not target:
        print("target area found")
        return
    articles = target.field.find_all('div',class_='col')
    if not articles:
        print("articles not found")
        return
    total=len(articles)
    print('articles found')
    print("total article found:",total)
    for item in articles:
        try:pubdate=item.find('time')['datetime']
        except:pubdate=None
        title=item.find('h3').text
        summary=item.find('p').text
        author=item.find('span').text
        img_src=item.find('img')['src']
        article = article(
            title=title,
            pubdate=pubdate,
            summary=summary,
            author=author,
            imgsrc=img_src
        )
        save(article)

if __name__ == __main__:
    soup=get_soup()
    try:
        extract(soup)
        print("Done")
        Except Exception as e:
        print