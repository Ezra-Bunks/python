import random

def simulate_world_cup():
    country_name = input("Enter your country's name: ")
    world_cup_year = 2026
    current_year = 2023
    has_won_world_cup = False
    team_skill = 50 # Initial skill level (out of 100)
    team_morale = 50 # Initial morale level (out of 100)

    print(f"\nWelcome, {country_name}! Your journey to the World Cup {world_cup_year} begins now.")
    print("You need to prepare your team for the ultimate challenge.")

    while current_year <= world_cup_year:
        print(f"\n--- Year {current_year} ---")
        print(f"Team Skill: {team_skill}/100, Team Morale: {team_morale}/100")

        if current_year == world_cup_year:
            print(f"It's {world_cup_year}, the World Cup year! Time for the final push!")

            win_chance = (team_skill + team_morale) / 2
            if win_chance >= 70 and random.randint(1, 100) <= win_chance:
                has_won_world_cup = True
                print(f"Congratulations! {country_name} has won the World Cup {world_cup_year}!")
                break
            else:
                print(f"Unfortunately, {country_name} did not win the World Cup {world_cup_year}. Better luck next time!")
                break

        print("\nWhat would you like to do this year?")
        print("1. Train Hard (Increase skill, risk morale)")
        print("2. Rest & Team Building (Increase morale, slight skill decay)")
        print("3. Try a 'Special Tactic' (High risk, high reward)")
        print("4. Do Nothing (Pass the year)")
        print("5. Give Up (End simulation)")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("You chose to train hard!")
            team_skill += random.randint(5, 15)
            team_morale -= random.randint(0, 5) # Training can be tough on morale
            if team_skill > 100: team_skill = 100
            if team_morale < 0: team_morale = 0
            print("Your team's skill has improved, but morale might be a bit low.")
            current_year += 1 # Increment year after action
            continue # Continue to the next year's loop iteration
        elif choice == '2':
            print("You chose rest and team building!")
            team_morale += random.randint(5, 10)
            team_skill -= random.randint(0, 3) # Slight skill decay if not training intensely
            if team_morale > 100: team_morale = 100
            if team_skill < 0: team_skill = 0
            print("Your team's morale is boosted, but skill might have slightly dipped.")
            current_year += 1
            continue #
        elif choice == '3':
            print("You decided to try a 'Special Tactic'...")
            if random.randint(1, 100) > 60: # 40% chance of success
                team_skill += 20
                team_morale += 10
                if team_skill > 100: team_skill = 100
                if team_morale > 100: team_morale = 100
                print("The special tactic paid off! Huge boost to skill and morale!")
            else:
                team_skill -= 15
                team_morale -= 15
                if team_skill < 0: team_skill = 0
                if team_morale < 0: team_morale = 0
                print("The special tactic backfired! Skill and morale took a hit.")
            current_year += 1
            continue
        elif choice == '4':
            print("You chose to do nothing this year. Time passes by...")
            pass # No specific action
            # Skill and morale might slightly decay due to inactivity
            team_skill -= random.randint(1, 3)
            team_morale -= random.randint(1, 2)
            if team_skill < 0: team_skill = 0
            if team_morale < 0: team_morale = 0
            current_year += 1
            continue
        elif choice == '5':
            print(f"{country_name} decided to give up on the World Cup dream.")
            break # Exit the loop
        else:
            print("Invalid choice. Please try again.")
            continue # Re-prompt for input for the same year.

    print("\n--- Simulation End ---")
    if has_won_world_cup:
        print(f"Congratulations, {country_name}! You are the champions of World Cup {world_cup_year}!")
    else:
        print(f"The journey for {country_name} to the World Cup {world_cup_year} has concluded.")
        print("Better luck in the next tournament!")

if __name__ == "__main__":
    simulate_world_cup()
