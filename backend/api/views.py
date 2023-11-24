from rest_framework.decorators import action
from rest_framework.response import Response
from segments.models import Users, Actions, SegmentsList
from .serializers import (
    UsersSerializer,
    ActionsSerializer,
    SegmentsListSerializer
)
from rest_framework import viewsets
from django.http import HttpResponse
import csv
from datetime import datetime


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_filtered_actions(self, request, user):
        actions_list = Actions.objects.filter(user=user)

        date_time_after_str = request.query_params.get('date_time_after')
        date_time_before_str = request.query_params.get('date_time_before')

        try:
            date_time_after = datetime.strptime(
                date_time_after_str, '%Y-%m-%d'
            ).date() if date_time_after_str else None
            date_time_before = datetime.strptime(
                date_time_before_str, '%Y-%m-%d'
            ).date() if date_time_before_str else None
        except ValueError:
            return None, Response(
                {"error": "Неверный формат даты. Используйте YYYY-MM-DD."},
                status=400
            )

        if date_time_after and date_time_before:
            actions_list = actions_list.filter(
                date_time__range=[date_time_after, date_time_before])

        return actions_list, None

    @action(detail=True, methods=['get'], url_path='date-filter')
    def search_in_detail(self, request, pk=None):
        user = self.get_object()
        actions_list, error_response = self.get_filtered_actions(request, user)
        if error_response:
            return error_response

        serializer = ActionsSerializer(actions_list, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='download-csv')
    def download_filtered_csv(self, request, pk=None):
        user = self.get_object()
        actions_list, error_response = self.get_filtered_actions(request, user)
        if error_response:
            return error_response

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename="filtered_actions.csv"'
        )

        writer = csv.writer(response)
        writer.writerow(['Action', 'Date', 'User'])

        for actions in actions_list:
            writer.writerow(
                [actions.action, actions.date_time, actions.user.nickname])

        return response


class SegmentsListViewSet(viewsets.ModelViewSet):
    queryset = SegmentsList.objects.all()
    serializer_class = SegmentsListSerializer
    lookup_field = 'slug'


class ActionsViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    http_method_names = ['get',]
