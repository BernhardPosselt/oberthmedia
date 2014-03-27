from oberthmedia.homepage.models import News

def news_processor(request):
    news = News.objects.all()

    if len(news) > 0:
        return {
            'news': news[0].message
        }
    else:
        return {
            'news': ''
        }