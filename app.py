from mongoengine import *
from models import *

connect('tumblelog')
ross = User(email='ross@example.com')
ross.first_name = 'Ross'
ross.last_name = 'Lawley'
ross.save()
# Below is the same as the 4 lines above
john = User(email='john@example.com', first_name='John', last_name='Lopez').save()


post1 = TextPost(title='Fun with MongoEngine', author=john)
post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()


[print(post.title) for post in Post.objects]

[print(post.content) for post in TextPost.objects]

for post in Post.objects:
    print(post.title)
    print('=' * len(post.title))

    if isinstance(post, TextPost):
        print(post.content)

    if isinstance(post, LinkPost):
        print('link: {}'.format(post.link_url))


for post in Post.objects(tags='mongodb'):
    print(post.title)


num_posts = Post.objects(tags='mongodb').count()
print('Found {} posts with tag "mongodb"'.format(num_posts))

