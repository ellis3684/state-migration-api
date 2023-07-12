from rest_framework import serializers
from statemigrations.models import StateMigration


class StateMigrationSerializer(serializers.ModelSerializer):
    estimate_lb = serializers.SerializerMethodField('get_estimate_lb')
    estimate_ub = serializers.SerializerMethodField('get_estimate_ub')

    # Credit to this SO answer for help with adding calculated fields to serializer:
    # https://stackoverflow.com/questions/22677070/additional-field-while-serializing-django-rest-framework
    def get_estimate_lb(self, obj):
        if int(obj.estimate - obj.margin_of_error) < 0:
            return 0
        else:
            return int(obj.estimate - obj.margin_of_error)

    def get_estimate_ub(self, obj):
        return int(obj.estimate + obj.margin_of_error)

    class Meta:
        model = StateMigration
        fields = ('previous_state', 'year', 'estimate', 'estimate_lb', 'estimate_ub')
