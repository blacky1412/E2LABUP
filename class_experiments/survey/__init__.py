from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='¿Qué edad tienes?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Hombre'], ['Female', 'Mujer'], ['Other', 'Otro']],
        label='¿Con qué género te identificas?',
        widget=widgets.RadioSelect,
    )
    gametheory =models.BooleanField(
        label= '¿Tenía conocimiento previo sobre teoría de juegos?',
        choices=[[True, 'Sí'],[False, 'No']], 
        widget=widgets.RadioSelect,
    )
    cooperate = models.IntegerField(
        min=1, max=5,
        label="Del 1 al 5, ¿qué tan cooperativo te consideras? (Donde 1 es muy poco cooperativo y 5 es muy cooperativo)",
        choices= [[1,1],[2,2],[3,3],[4,4],[5,5]],
        widget=widgets.RadioSelectHorizontal,
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','gametheory', 'cooperate']





page_sequence = [Demographics]
