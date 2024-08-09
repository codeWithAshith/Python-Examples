def get_input(word_type: str):
    user_input = input(f"Enter the {word_type}: ")
    return user_input


person_name = get_input("person's name")
cat_name = get_input("cat's name")
place = get_input("place")

story = f"""
One sunny morning, {person_name} was strolling through {place} when they heard a soft meow. Looking around, {person_name} saw a little cat sitting under a tree.

{person_name}: "Hello there, little one. What's your name?"
Cat: "My name is {cat_name}. What brings you here?"
{person_name}: "I'm just enjoying the weather. What about you, {cat_name}?"
{cat_name}: "I'm just exploring {place} and looking for someone to spend time with."
{person_name}: "I'd love to spend time with you, {cat_name}. Let's explore together!"

And so, {person_name} and {cat_name} spent the day together, exploring {place} and enjoying each other's company. 
The end.
"""

print(story)
