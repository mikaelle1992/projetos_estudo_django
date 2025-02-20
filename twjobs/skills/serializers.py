from rest_framework import serializers

from skills.models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        # fields = ("id", "name")
        