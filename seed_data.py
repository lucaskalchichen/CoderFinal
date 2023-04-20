
from progres_pick.models import Post,User

for _ in range(0,10):
    Post(nombre="zyzz", image="progres_pick/static/progres_pick/assets/zyzz.jpg" ,
    description="Volumen",publisher = User.objects.get(id=1)
    ).save()
