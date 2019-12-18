

class World:

    def _init_(self):
        pass

    # put unit_id in path_id in position 'index' all spells of one kind have the same id
    def cast_unit_spell(self, unit_id, path_id, index, spell, spell_id):
        pass

    # cast spell in the cell 'center'
    def cast_area_spell(self, center, spell, spell_id):
        pass

    # returns a list of units the spell casts effects on
    def get_area_spell_targets(self, center, spell, spell_id):
        pass

    # every once in a while you can upgrade, this returns the remaining time for upgrade
    def get_remaining_turns_to_upgrade(self):
        pass

    # every once in a while a spell is given this remains the remaining time to get new spell
    def get_remaining_turns_to_get_spell(self):
        pass

    # returns area spells that are casted in last turn and returns other players spells also
    def get_cast_area_spell(self, player_id):
        pass

    # returns unit spells that are casted in last turn and returns other players spells also
    def get_cast_unit_spell(self, player_id):
        pass

    # returns a list of units that are deployed by 'player_id' in the "last turn"
    def get_deployed_units(self, player_id):
        pass

    # returns a list of spells casted on a cell
    def get_active_spells_on_cell(self, cell):
        pass

    # returns the token of the upgrade you can do
    def get_upgrade_token_number(self):
        pass

    # get current available spells
    def get_spellsO(self):
        pass

    # returns the spell given in that turn
    def get_received_spell(self):
        pass

    # returns the spell given in that turn to friend
    def get_friend_received_spell(self):
        pass

    def get_my_id(self):
        pass

    def get_friend_id(self):
        pass

    # in the first turn 'deck picking' give unit_ids or list of unit names to pick in that turn
    def choose_deck(self, units):
        pass

    # returns a cell that is the fortress of player with player_id
    def get_player_position(self, player_id):
        pass

    # return a list of paths starting from the fortress of player with player_id
    # the beginning is from player_id fortress cell
    def get_paths_from_player(self, player_id):
        pass

    # returns the path from player_id to its friend beginning from player_id's fortress
    def get_path_to_friend(self, player_id):
        pass

    def get_map_height(self):
        pass

    def get_map_width(self):
        pass

    # return a list of paths crossing one cell
    def get_paths_crossing_cell(self, cell):
        pass

    # return units of player that are currently in map
    def get_player_units(self, player_id):
        pass

    # return a list of units in a cell
    def get_cell_units(self, cell):
        pass

    # return the shortest path from player_id fortress to cell
    # this path is in the available path list
    def get_shortest_path_to_cell(self, player_id, cell):
        pass

    # returns the limit of ap for each player
    def get_max_ap(self):
        pass

    # get remaining ap
    def get_remaining_ap(self):
        pass

    # returns a list of units in hand
    def get_hand(self):
        pass

    # returns a list of units in deck
    def get_deck(self):
        pass

    # place unit with type_id in path_id
    def play_unit(self, type_id, path_id):
        pass

    # return the number of turns passed
    def get_current_turn(self):
        pass

    # return the limit of turns
    def get_max_turns(self):
        pass

    # return the time left to pick units and put in deck in the first turn
    def get_pick_timout(self):
        pass

    # a constant limit for each turn
    def get_turn_timout(self):
        pass

    # returns the time left for turn (miliseconds)
    def get_remaining_time(self):
        pass

    # returns the health point remaining for each player
    def get_player_hp(self):
        pass