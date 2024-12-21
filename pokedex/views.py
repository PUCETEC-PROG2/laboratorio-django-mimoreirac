from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    pokemons = Pokemon.objects.order_by('type')
    trainers = Trainer.objects.order_by('last_name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))