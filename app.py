# # def user_choice():
# #     choice = "WRONG!"
# #     acceptable_range = range(0, 11)
# #     within_range = False

# #     while choice.isdigit() == False or within_range == False:
# #         choice = input("Please enter a number (0-10): ")

# #         if choice.isdigit() == False:
# #             print("Sorry that is not a digit!")

# #         if choice.isdigit():
# #             if int(choice) in acceptable_range:
# #                 within_range = True
# #             else:
# #                 print("Sorry, you are out of the range of 0-10.")
# #                 pass
            

# #     return int(choice)

# game_list = [0,1,2]

# def display_game(game_list):
#     print("Here is the current list: ")
#     print(game_list)

# def row_choice():
#     choice = "Wrong."

#     while choice not in ["0", "1", "2"]:
#         choice = input("Pick a position to replace (0,1,2): ")

#         if choice not in ["0", "1", "2"]:
#             # clear_output()
#             print("Sorry, but you did not choose a valid position (0,1,2)")
        
#     return int(choice)

# def replacement_choice(game_list, row):
#     user_placement = input("Type a string to place at the position: ")
#     game_list[row] = user_placement
#     return game_list

# def gameon_choice():
#     choice = "Wrong."

#     while choice not in ["y", "n"]:
#         choice = input("Would you like to keep playing? (y or n): ")

#         if choice.lower() not in ["y", "n"]:
#             # clear_output()
#             print("Sorry, I didn't understand. Please make sure to choose y or n.")

#         if choice.lower() == "y":
#             return True
#         else:
#             return False

# game_on = True
# game_list = [0,1,2]

# while game_on:
#     display_game(game_list)
#     row = row_choice()
#     game_list = replacement_choice(game_list, row)
#     display_game(game_list)
#     game_on = gameon_choice()