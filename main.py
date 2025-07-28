# 📚 Step 1: Define an empty list to hold books

library = []


# 🔁 Step 2: Use a for loop to get book entries from the user
# 💡 Use a tuple to represent an individual book in the list

print("Enter detalis for five books ")

for i in range(5): 
  print(f"Book {i+1}")
  title=input("Enter title: ")
  Author=input("Enter author: ")
  year=input("Enter year: ")
  genre=input("Enter genre: ")
  
  book = (title , Author , year, genre)
  library.append(book)

# 📄 Step 3: Print all books nicely

  print("\n Here are the books in Library:")
  for book in library:
      print(f"Title of the book: {book[-4]} | Author of the book: {book[-3]} | Year of the book: {book[-2]} | Genre of of the book: {book[-1]}")
    
# 🔍 Step 4: Search books by author

search_author = input("\nEnter author name to search for their books: ")
print(f"\nBooks by {search_author}:")
found = False
for book in library:
  if book[-3].lower() == search_author.lower():
    print(f"- {book[-4]} ({book[-2]}) [{book[-1]}]")
    found = True
    if not found:
        print("No books found by that author.")

# 🔎 Step 5: Filter books by year

filter_year = int(input("\nEnter a year to find books published after it: "))
print(f"\nBooks published after {filter_year}:")
found = False
for book in library:
  if book[-2] > filter_year:
    print(f"- {book[-4]} by {book[-3]} ({book[-2]}) [{book[-1]}]")
found = True
if not found :
    print(f"No books found that was published after the year:{filter_year}")

# 🧠 Step 6: Summary with stats

print("\n Summary")
print(f"Total books: {len(library)}")

genres = []
for book in library:
    genres.append(book[3])

unique_genres = list(set(genres))  # Get unique genres using set()
print(f"Unique genres in library: {', '.join(unique_genres)}")


