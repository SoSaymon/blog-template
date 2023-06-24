from django.test import TestCase

from blog.models import Post, User, Tag, Category, Comment


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


class PostModelTest(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUpTestData(cls) -> None:
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_post_content(self) -> None:
        posts = Post.objects.all()

        self.assertEqual(posts.count(), self.test_data.num_of_posts)

        for post in posts:
            self.assertEqual(post.title, self.test_data.posts[post.id - 1]['title'])
            self.assertEqual(post.content, self.test_data.posts[post.id - 1]['content'])
            self.assertEqual(post.author, User.objects.get(name=self.test_data.posts[post.id - 1]['author']))
            self.assertEqual(post.category, Category.objects.get(name=self.test_data.posts[post.id - 1]['category']))
            self.assertEqual(post.tags.count(), len(self.test_data.posts[post.id - 1]['tags']))
            for tag in post.tags.all():
                self.assertIn(tag.name, self.test_data.posts[post.id - 1]['tags'])

    def test_post_str(self) -> None:
        posts = Post.objects.all()

        for post in posts:
            self.assertEqual(str(post), post.title)

    # TODO: Uncomment when views are ready
    # def test_post_get_absolute_url(self) -> None:
    #     posts = Post.objects.all()
    #
    #     for post in posts:
    #         self.assertEqual(post.get_absolute_url(), f'/blog/{post.id}/')

    def test_post_display_tags(self) -> None:
        posts = Post.objects.all()

        for post in posts:
            self.assertEqual(post.display_tags(), ', '.join(self.test_data.posts[post.id - 1]['tags']))


class UserModelTest(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUpTestData(cls) -> None:
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_user_content(self) -> None:
        users = User.objects.all()

        self.assertEqual(users.count(), self.test_data.num_of_users)

        for user in users:
            self.assertEqual(user.name, self.test_data.usernames[user.id - 1]['name'])
            self.assertEqual(user.email, self.test_data.usernames[user.id - 1]['name'] + '@example.com')
            self.assertEqual(user.bio, 'I am ' + self.test_data.usernames[user.id - 1]['name'])
            self.assertEqual(user.role, self.test_data.usernames[user.id - 1]['role'])

    def test_user_str(self) -> None:
        users = User.objects.all()

        for user in users:
            self.assertEqual(str(user), user.name)

    # TODO: Uncomment when views are ready
    # def test_user_get_absolute_url(self) -> None:
    #     users = User.objects.all()
    #
    #     for user in users:
    #         self.assertEqual(user.get_absolute_url(), f'/blog/author/{user.id}/')

    def test_user_get_role(self) -> None:
        users = User.objects.all()

        for user in users:
            self.assertEqual(user.get_role(), self.test_data.usernames[user.id - 1]['role'])

    def test_user_get_role_verbose(self) -> None:
        users = User.objects.all()

        for user in users:
            self.assertEqual(user.get_role_verbose(), self.test_data.usernames[user.id - 1]['role'].capitalize())

    def test_user_get_posts(self) -> None:
        users = User.objects.all()

        for user in users:
            self.assertEqual(user.get_posts().count(), Post.objects.filter(author=user).count())
            for post in user.get_posts():
                self.assertEqual(post.author, user)


class TagModelTest(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUpTestData(cls) -> None:
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_tag_content(self) -> None:
        tags = Tag.objects.all()

        self.assertEqual(tags.count(), self.test_data.num_of_tags)

        for tag in tags:
            self.assertEqual(tag.name, self.test_data.tags[tag.id - 1])

    def test_tag_str(self) -> None:
        tags = Tag.objects.all()

        for tag in tags:
            self.assertEqual(str(tag), tag.name)

    # TODO: Uncomment when views are ready
    # def test_tag_get_absolute_url(self) -> None:
    #     tags = Tag.objects.all()
    #
    #     for tag in tags:
    #         self.assertEqual(tag.get_absolute_url(), f'/blog/tag/{tag.id}/')


class CategoryModelTest(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUpTestData(cls) -> None:
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_category_content(self) -> None:
        categories = Category.objects.all()

        self.assertEqual(categories.count(), self.test_data.num_of_categories)

        for category in categories:
            self.assertEqual(category.name, self.test_data.categories[category.id - 1])

    def test_category_str(self) -> None:
        categories = Category.objects.all()

        for category in categories:
            self.assertEqual(str(category), category.name)

    # TODO: Uncomment when views are ready
    # def test_category_get_absolute_url(self) -> None:
    #     categories = Category.objects.all()
    #
    #     for category in categories:
    #         self.assertEqual(category.get_absolute_url(), f'/blog/category/{category.id}/')


class CommentModelTest(TestCase):
    APPROVED_COMMENT = True
    test_data = SetUpTestData()

    @classmethod
    def setUpTestData(cls) -> None:
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_comment_content(self) -> None:
        comments = Comment.objects.all()

        self.assertEqual(comments.count(), self.test_data.num_of_comments)

        for comment in comments:
            self.assertEqual(comment.author, User.objects.get(name=self.test_data.comments[comment.id - 1]['author']))
            self.assertEqual(comment.post, Post.objects.get(title=self.test_data.comments[comment.id - 1]['post']))
            self.assertEqual(comment.content, self.test_data.comments[comment.id - 1]['content'])

    def test_comment_str(self) -> None:
        comments = Comment.objects.all()

        for comment in comments:
            self.assertEqual(str(comment), comment.content)

    def test_comment_approved(self) -> None:

        comments = Comment.objects.all()

        for comment in comments:
            comment.approve()
            self.assertEqual(comment.approved, self.APPROVED_COMMENT)
