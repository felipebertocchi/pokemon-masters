import random

class Pokemon:
  def __init__(self, name, level, type):
    self.name = name
    self.level = level
    self.health = 5 * level
    self.max_health = 5 * level
    self.type = type
    self.is_knocked_out = False

  def __repr__(self):
    return """\
{}
    a {} type pokémon.
    Lvl = {}
    Health = {}/{}
    """.format(self.name, self.type, self.level, self.health, self.max_health)

  def lose_health(self, amount):
    self.health -= amount
    if self.health > 0:
      if self.health > (0.1 * self.max_health):
        print("  {} now has {} health\n".format(self.name, self.health))
      else:
        print("  {} now has {} health\n  Critical condition!\n".format(self.name, self.health))
    else:
      print("  {} now has 0 health\n".format(self.name))
      self.is_knocked_out = True
      print("  {} was knocked out!\n".format(self.name))


  def heal(self, amount):
    if (self.health + amount) > self.max_health:
      self.health = self.max_health
    else:
      self.health += amount
    print("{} now has {} health".format(self.name, self.health))

  def revive(self):
    if self.is_knocked_out:
      self.is_knocked_out = False
      self.health = self.max_health / 2    
      print("{} was revived using a life stone!".format(self.name))
    else:
      print("Your pokémon doesn't need to be revived")

  def attack(self, enemy_pokemon):
    if self.is_knocked_out == False and enemy_pokemon.is_knocked_out == False:
      if self.type == enemy_pokemon.type:
        damage_dealt = round(random.uniform(0.2,0.8) * 3 * self.level)
        print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
        enemy_pokemon.lose_health(damage_dealt)

      if self.type == "Fire":
        if enemy_pokemon.type == "Grass":
          damage_dealt = 2 * round(random.uniform(0.2,0.8) * 3 * self.level)
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's super effective!\n")
          enemy_pokemon.lose_health(damage_dealt)
        elif enemy_pokemon.type == "Water":
          damage_dealt = round(0.5 * (random.uniform(0.2,0.8) * 3 * self.level))
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's not so effective...\n")
          enemy_pokemon.lose_health(damage_dealt)

      if self.type == "Water":
        if enemy_pokemon.type == "Fire":
          damage_dealt = 2 * round(random.uniform(0.2,0.8) * 3 * self.level)
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's super effective!\n")
          enemy_pokemon.lose_health(damage_dealt)
        elif enemy_pokemon.type == "Grass":
          damage_dealt = round(0.5 * (random.uniform(0.2,0.8) * 3 * self.level))
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's not so effective...\n")
          enemy_pokemon.lose_health(damage_dealt)

      if self.type == "Grass":
        if enemy_pokemon.type == "Water":
          damage_dealt = 2 * round(random.uniform(0.2,0.8) * 3 * self.level)
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's super effective!\n")
          enemy_pokemon.lose_health(damage_dealt)
        elif enemy_pokemon.type == "Fire":
          damage_dealt = round(0.5 * (random.uniform(0.2,0.8) * 3 * self.level))
          print("{} deals {} points of damage to {}".format(self.name, damage_dealt, enemy_pokemon.name))
          print("It's not very effective...\n")
          enemy_pokemon.lose_health(damage_dealt)


class Trainer:
  def __init__(self, name, pokemon_list, potions):
    self.name = name
    self.pokemon_list = pokemon_list
    self.current_pokemon = pokemon_list[0]
    self.potions = potions
    self.battle_active = False

  def __repr__(self):
    return """\
Trainer {name}
  current pokemon: {current_pokemon} level {lvl}
    """.format(name = self.name, current_pokemon = self.current_pokemon.name, lvl = self.current_pokemon.level)

  def switch_pokemons(self):
    healthy_pokemons = []
    for pokemon in self.pokemon_list:
      if pokemon.is_knocked_out == False:
        healthy_pokemons.append(pokemon)
        
    if len(healthy_pokemons) == 0:
      print("no more pokemon available, {} loses!".format(self.name))
      self.battle_active = True

    else:
      for pokemon in healthy_pokemons:
        print("{trainer}: Go {name}, it's your turn!\n".format(trainer = self.name, name = pokemon.name))
        self.current_pokemon = pokemon

  def engage(self, enemy_trainer):
    
    r = 0
    self.battle_active = False
    enemy_trainer.battle_active = False
    while self.battle_active == False and enemy_trainer.battle_active == False:
      my_pokemon = self.current_pokemon
      enemy_pokemon = enemy_trainer.current_pokemon
      r += 1
      print("== Battle Phase {} ==".format(r))

      if my_pokemon.is_knocked_out:
        self.switch_pokemons()
        my_pokemon = self.current_pokemon

      if enemy_pokemon.is_knocked_out:
        enemy_trainer.switch_pokemons()
        enemy_pokemon = enemy_trainer.current_pokemon
      
      my_pokemon.attack(enemy_pokemon)
      enemy_pokemon.attack(my_pokemon)


  def use_potion(self):
    if self.potions > 0 and (self.current_pokemon.health < self.current_pokemon.max_health):
      self.current_pokemon.heal(0.3 * self.current_pokemon.max_health)
    elif self.potions == 0:
      print("You have no potions left!")
    elif self.current_pokemon.health == self.current_pokemon.max_health:
      print("Your pokemon already has max health")

#########################################################

class Charmander(Pokemon):
  def __init__(self, level = 3):
    super().__init__("Charmander", level, "Fire")

class Squirtle(Pokemon):
  def __init__(self, level = 3):
    super().__init__("Squirtle", level, "Water")

class Bulbasaur(Pokemon):
  def __init__(self, level = 3):
    super().__init__("Bulbasaur", level, "Grass")

# print(Charmander())

# Charmander().attack(Bulbasaur())
# Squirtle().attack(Bulbasaur())

#########################################################

a = Charmander(3)
b = Squirtle(3)
c = Bulbasaur(5)
d = Charmander(4)

ash = Trainer("Ash", [a, b], 2)
print(ash)

gary = Trainer("Gary", [c, d], 2)
print(gary)

ash.engage(gary)

