import db
import scraputils


def save_data(pages=1):
    news = scraputils.get_news("https://news.ycombinator.com/newest", pages)
    s = db.session()
    for i in news:
        obj = db.News(
            title=i["title"],
            author=i["author"],
            url=i["url"],
            comments=i["comments"],
            points=i["points"],
        )
        print(f"Preparing news extract {i}, id: {obj.id}, title: {obj.title}")
        s.add(obj)
        s.commit()
        print(f"Committed extract {i} at id {obj.id}")


save_data(36)
