from rest_framework.routers import DefaultRouter
from .views import AlunoViewsSet, DisciplinaViewSet, BoletimViewSet, NotasViewSet

router = DefaultRouter()
router.register(r'aluno', AlunoViewsSet, 'aluno')
router.register(r'disciplina', DisciplinaViewSet, 'disciplina')
router.register(r'boletim', BoletimViewSet, 'boletim')
router.register(r'notas', NotasViewSet, 'notas')

aluno_urls = router.urls