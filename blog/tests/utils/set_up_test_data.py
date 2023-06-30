from blog.models import Post, Category, Tag, Comment, User


class SetUpTestData:
    # Creation data
    user_data: list[dict] = [
        {
            'username': 'test_user_1',
            'email': 'test_user_1@test.dev',
            'bio': 'Test user 1 bio',
            'role': 'author',
            'is_staff': True,
            'is_superuser': False,
            'is_active': True,
        },
        {
            'username': 'test_user_2',
            'email': 'test_user_2@test.dev',
            'bio': 'Test user 2 bio',
            'role': 'moderator',
            'is_staff': True,
            'is_superuser': False,
            'is_active': True,
        },
        {
            'username': 'test_user_3',
            'email': 'test_user_3@test.dev',
            'bio': 'Test user 3 bio',
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        },
        {
            'username': 'test_user_4',
            'email': 'test_user_4@test.dev',
            'bio': 'Test user 4 bio',
            'role': 'user',
            'is_staff': False,
            'is_superuser': False,
            'is_active': True,
        },
    ]

    category_data: list[dict] = [
        {
            'name': 'Test category 1',
        },
        {
            'name': 'Test category 2',
        },
        {
            'name': 'Test category 3',
        },
        {
            'name': 'Test category 4',
        },
    ]

    tag_data: list[dict] = [
        {
            'name': 'Test tag 1',
        },
        {
            'name': 'Test tag 2',
        },
        {
            'name': 'Test tag 3',
        },
        {
            'name': 'Test tag 4',
        },
    ]

    post_data: list[dict] = [
        {
            'title': 'Test post 1',
            'content': 'Test post 1 content',
            'author': 'test_user_1',
            'category': 'Test category 1',
            'tags': ['Test tag 1', 'Test tag 2'],
        },
        {
            'title': 'Test post 2',
            'content': 'Test post 2 content',
            'author': 'test_user_1',
            'category': 'Test category 2',
            'tags': ['Test tag 2', 'Test tag 3'],
        },
        {
            'title': 'Test post 3',
            'content': 'Test post 3 content',
            'author': 'test_user_1',
            'category': 'Test category 3',
            'tags': ['Test tag 3', 'Test tag 4'],
        },
        {
            'title': 'Test post 4',
            'content': 'Test post 4 content',
            'author': 'test_user_1',
            'category': 'Test category 4',
            'tags': ['Test tag 4', 'Test tag 1'],
        },
    ]

    comment_data: list[dict] = [
        {
            'content': 'Test comment 1 content',
            'author': 'test_user_1',
            'post': 'Test post 1',
        },
        {
            'content': 'Test comment 2 content',
            'author': 'test_user_2',
            'post': 'Test post 2',
        },
        {
            'content': 'Test comment 3 content',
            'author': 'test_user_3',
            'post': 'Test post 3',
        },
        {
            'content': 'Test comment 4 content',
            'author': 'test_user_4',
            'post': 'Test post 4',
        },
    ]

    def __init__(self):
        self.create_users()
        self.create_categories()
        self.create_tags()
        self.create_posts()
        self.create_comments()

    # Creation methods
    def create_users(self):
        for user in self.user_data:
            User.objects.create_user(**user)

    def create_categories(self):
        for category in self.category_data:
            Category.objects.create(**category)

    def create_tags(self):
        for tag in self.tag_data:
            Tag.objects.create(**tag)

    def create_posts(self):
        for post in self.post_data:
            author = User.objects.get(username=post['author'])
            category = Category.objects.get(name=post['category'])
            tags = [Tag.objects.get(name=tag_name) for tag_name in post['tags']]
            post_instance = Post.objects.create(title=post['title'], content=post['content'], author=author,
                                                category=category)
            post_instance.tags.set(tags)

    def create_comments(self):
        for comment in self.comment_data:
            comment['author'] = User.objects.get(username=comment['author'])
            comment['post'] = Post.objects.get(title=comment['post'])
            Comment.objects.create(**comment)

    # Deletion methods

    @staticmethod
    def delete_users():
        User.objects.all().delete()

    @staticmethod
    def delete_categories():
        Category.objects.all().delete()

    @staticmethod
    def delete_tags():
        Tag.objects.all().delete()

    @staticmethod
    def delete_posts():
        Post.objects.all().delete()

    @staticmethod
    def delete_comments():
        Comment.objects.all().delete()
