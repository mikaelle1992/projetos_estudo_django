from rest_framework.viewsets import ModelViewSet
 
from .models import Skill
from .serializers import SkillSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # def list(self, request):
    #     skills = Skill.objects.all()
    #     serializer = SkillSerializer(skills, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = SkillSerializer(data= request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def retriave(self, request, pk=None):
    #     skill = get_object_or_404(Skill, pk=pk)
    #     serializer = SkillSerializer(skill)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     skill = get_object_or_404(Skill, pk=pk)
    #     serializer = SkillSerializer(skill, data= request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def destroy(self, request, pk=None):
    #     skill = get_object_or_404(Skill, pk=pk)
    #     skill.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

