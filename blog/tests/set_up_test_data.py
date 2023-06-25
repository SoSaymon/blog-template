from blog.models import Post, Category, Tag, Comment, User


class SetUpTestData:
    # Creation data
    num_of_users: int = 0
    num_of_tags: int = 0
    num_of_categories: int = 0
    num_of_posts: int = 0
    num_of_comments: int = 0

    # Users, tags, categories and posts data
    usernames: list[{str, str}] = [
        {'name': 'admin', 'role': 'admin'},
        {'name': 'author', 'role': 'author'},
        {'name': 'moderator', 'role': 'moderator'},
        {'name': 'user', 'role': 'user'},
    ]

    tags: list[str] = ['tag1', 'tag2', 'tag3']
    categories: list[str] = ['category1', 'category2', 'category3']
    posts: list[{str, str, str, str, list[str], str}] = [
        {'title': 'post1', 'content': 'content1', 'author': 'admin', 'tags': ['tag1', 'tag2'], 'category': 'category1'},
        {'title': 'post2', 'content': 'content2', 'author': 'author', 'tags': ['tag2', 'tag3'],
         'category': 'category2'},
        {'title': 'post3', 'content': 'content3', 'author': 'moderator', 'tags': ['tag1', 'tag3'],
         'category': 'category3'},
    ]
    comments: list[{str, str, str}] = [
        {'post': 'post1', 'author': 'admin', 'content': 'comment1'},
        {'post': 'post2', 'author': 'author', 'content': 'comment2'},
        {'post': 'post3', 'author': 'moderator', 'content': 'comment3'},
        {'post': 'post3', 'author': 'user', 'content': 'comment4'},
    ]

    @staticmethod
    def create_users(self, names: list[dict[str, str]]) -> None:
        for name_data in names:
            User.objects.create(
                name=name_data['name'],
                email=name_data['name'] + '@example.com',
                bio='I am ' + name_data['name'],
                role=name_data['role']
            )
            self.num_of_users += 1

    @staticmethod
    def create_tags(self, names: list[str]) -> None:
        for name in iter(names):
            Tag.objects.create(name=name)
            self.num_of_tags += 1

    @staticmethod
    def create_categories(self, names: list[str]) -> None:
        for name in iter(names):
            Category.objects.create(name=name)
            self.num_of_categories += 1

    @staticmethod
    def create_posts(self, posts: list[dict[str, any]]) -> None:
        for post in posts:
            post_obj = Post.objects.create(
                title=post['title'],
                content=post['content'],
                author=User.objects.get(name=post['author']),
                category=Category.objects.get(name=post['category']),
            )
            post_obj.tags.set(Tag.objects.filter(name__in=post['tags']))
            self.num_of_posts += 1

    @staticmethod
    def create_comments(self, comments: list[dict[str, str, str]]) -> None:
        for comment in comments:
            Comment.objects.create(
                post=Post.objects.get(title=comment['post']),
                author=User.objects.get(name=comment['author']),
                content=comment['content']
            )
            self.num_of_comments += 1
