import datetime
from django.test import TestCase
from segments.models import SegmentsList, Users, Actions
from .serializers import (
    SegmentsListSerializer,
    UsersSerializer,
    ActionsSerializer
)


class SegmentsListSerializerTestCase(TestCase):
    def test_serializer_contains_expected_fields(self):
        serializer = SegmentsListSerializer()
        expected_fields = ['id', 'title', 'slug', 'users']
        self.assertEqual(list(serializer.fields.keys()), expected_fields)


class UsersSerializerTestCase(TestCase):
    def setUp(self):
        self.segment1 = SegmentsList.objects.create(title='Segment 1')
        self.segment2 = SegmentsList.objects.create(title='Segment 2')
        self.user = Users.objects.create(nickname='draftpick#1')
        self.action1 = Actions.objects.create(
            user=self.user,
            segment=self.segment1,
            action='Action 1',
            date_time=datetime.date.today()
        )
        self.action2 = Actions.objects.create(
            user=self.user,
            segment=self.segment2,
            action='Action 2',
            date_time=datetime.date.today()
        )

    def test_create_user_with_segments_creates_actions(self):
        data = {
            'nickname': 'draftpick#2',
            'segments': [self.segment1.title, self.segment2.title]
        }
        serializer = UsersSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        actions = Actions.objects.filter(user=user)
        self.assertEqual(actions.count(), 2)


class ActionsSerializerTestCase(TestCase):
    def test_serializer_contains_expected_fields(self):
        serializer = ActionsSerializer()
        expected_fields = ['id', 'action', 'date_time', 'user', 'segment']
        self.assertEqual(list(serializer.fields.keys()), expected_fields)
