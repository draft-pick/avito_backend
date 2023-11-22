from rest_framework import serializers
from segments.models import Users, Actions, SegmentsList


class SegmentsListSerializer(serializers.ModelSerializer):
    """Добавление нового сегмента."""
    class Meta:
        model = SegmentsList
        fields = '__all__'
        lookup_field = 'slug'


class UsersSerializer(serializers.ModelSerializer):
    """
        Создание нового пользователя.
        Выбор объектов из модели SegmentsList.
        Переопределение методов update и create
        с возможностью логирования модели Actions.
    """
    segments = serializers.SlugRelatedField(
        queryset=SegmentsList.objects.all(), many=True, slug_field='title'
    )
    actions = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'nickname', 'segments', 'actions']

    def create(self, validated_data):
        segments_data = validated_data.pop('segments', [])
        user = super().create(validated_data)
        for segment in segments_data:
            Actions.objects.create(
                user=user,
                segment=segment,
                action=f'{segment.title} - added'
            )
        user.segments.set(segments_data)
        return user

    def update(self, instance, validated_data):
        segments_data = validated_data.pop('segments', [])
        instance = super().update(instance, validated_data)
        for segment in segments_data:
            if segment not in instance.segments.all():
                Actions.objects.create(
                    user=instance,
                    segment=segment,
                    action=f'{segment.title} - added'
                )
        for segment in instance.segments.all():
            if segment not in segments_data:
                Actions.objects.create(
                    user=instance,
                    segment=segment,
                    action=f'{segment.title} - removed'
                )
        instance.segments.set(segments_data)
        return instance

    def get_actions(self, obj):
        actions = obj.actions.values(
            'action',
            'date_time',
        )
        return actions


class ActionsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Actions."""
    class Meta:
        model = Actions
        fields = '__all__'
