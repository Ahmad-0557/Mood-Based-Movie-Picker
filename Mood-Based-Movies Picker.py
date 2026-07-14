genres = {
    "happy": ["comedy", "romance", "musical"],
    "sad": ["drama", "tragedy", "melodrama"],
    "scary": ["horror", "thriller", "suspense"],
    "exciting": ["action", "adventure", "sci-fi"],
}
userinput = input("Enter a mood (happy, sad, scary, exciting): ").lower()
if userinput in genres:
    print("Here are some genres that match your mood:", genres[userinput])
else:
    print("Sorry, we don't have any genres for that mood.")