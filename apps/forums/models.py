from forums.base_forum import AbstractBaseForum


class Forum(AbstractBaseForum):
    class Meta(AbstractBaseForum.Meta):
        swappable = "FORUM_MODEL"
