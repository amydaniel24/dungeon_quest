import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        name = input("Enter your name: ").strip() or "Adventurer"

        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }

        # TODO: Return the dictionary
        return player
    



    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                 {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures ={
                    "a gold pocket watch with the initials D.A.": 5,
                    "a gaudy gold ring studded with diamonds with a faint magic aura, it causes memory loss, with previous day's events forgotten": 10,
                    "a diary of a teenaged girl. Contains much gossip.": 7,
                    "An under tensioned spring": 9,
                    "a photograph of a cat": 4
                }
        # TODO: Return the dictionary
        return treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
    print("\n" + "-" * 40)
    print(f"You are in room {room_number}.")
    print("What would you like to do?")
    print("1. Search for treasure")
    print("2. Move to next room")
    print("3. Check health and inventory")
    print("4. Quit the game")

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
if outcome == "treasure":
            found = random.choice(list(treasures.keys()))
            player["inventory"].append(found)
            print(f"\nYou found a **{found}**! (+{treasures[found]} value)")
else:
            # trap
            player["health"] = max(0, player["health"] - 2)
            print("\nOh no! You found a trap and lost 2 health!")
            if player["health"] == 0:
                print("Ouch, I hope no one's watching you play . . .")

def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”

def check_status(player):
       
        print("\n=== Status ===")
        print(f"Health: {player['health']}")
        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")
    
def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."

def end_game(player, treasures):
       
        total_value = sum(treasures.get(item, 0) for item in player["inventory"])

        print("\n" + "=" * 40)
        print("              GAME SUMMARY")
        print("=" * 40)
        print(f"Adventurer: {player['name']}")
        print(f"Final Health: {player['health']}")
        if player["inventory"]:
            print("Collected Treasures:")
            for item in player["inventory"]:
                print(f" - {item} (+{treasures.get(item, 0)})")
        else:
            print("Collected Treasures: (none)")
        print(f"Total Treasure Value: {total_value}")
        print("=" * 40)
        print("My God, Adventurer! That was pure madness! I don't know what to say; get out of there, the mission's over!")


def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
