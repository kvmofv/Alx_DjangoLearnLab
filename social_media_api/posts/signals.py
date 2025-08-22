from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Like, Comment
from accounts.models import Follow
from notifications.models import Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.user:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(instance.post),
            object_id=instance.post.id
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.user:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.user,
            verb="commented on your post",
            content_type=ContentType.objects.get_for_model(instance.post),
            object_id=instance.post.id
        )

@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created and instance.following != instance.follower:
        Notification.objects.create(
            recipient=instance.following,
            actor=instance.follower,
            verb="started following you",
            content_type=ContentType.objects.get_for_model(instance.following),
            object_id=instance.following.id
        )
