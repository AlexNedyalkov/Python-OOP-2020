'''

The Player class should also have two methods:
    • add_skill(skill_name, mana_cost)
        ◦ Add the skill to the collection. Return "Skill {skill_name} added to the collection of the player {player_name}"
        ◦ If the skill is already in the collection, return "Skill already added"

    • player_info()
        ◦ Returns the player's information, including his/her skills, in this format:
"Name: {player_name}
 Guild: {guild_name}
 HP: {hp}
 MP: {mp}
 === {skill_name_1} – {skill_mana_cost}
 === {skill_name_2} – {skill_mana_cost}
 ...
 === {skill_name_N} – {skill_mana_cost}"

The Guild class receive a name {string}. It creates a list of players (empty by initialization). The class also has 3 methods:
    • assign_player(player: Player)
        ◦ Add the player to the guild. Return "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
        ◦ If the player is already in the guild, return "Player {player_name} is already in the guild."
        ◦ If the player is in another guild, return "Player {player_name} is in another guild."

    • kick_player(player_name: String)
        ◦ Remove the player to the guild. Return "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class.
        ◦ If the isn't a player with that name in the guild, return "Player {player_name} is not in the guild."

    • guild_info()
        ◦ Returns the guild's information, including the players in the guild, in this format:
"Guild: {guild_name}
 {player's info}
"
'''

class Player:

    def __init__(self, name, hp, mp):

        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

