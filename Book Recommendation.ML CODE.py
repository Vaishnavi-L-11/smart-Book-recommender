# ==========================================================
#                     BOOK BUDDY
#              Book Recommendation System
# ==========================================================

# Book data
books = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy",
        "rating": 4.8
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy",
        "rating": 4.7
    },
    {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "category": "Fantasy",
        "rating": 4.6
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Adventure",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "category": "Dystopian",
        "rating": 4.4
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "category": "Dystopian",
        "rating": 4.5
    },
    {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "category": "Historical",
        "rating": 4.4
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "Self Development",
        "rating": 4.6
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "category": "Self Development",
        "rating": 4.3
    },
    {
        "title": "Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "category": "Mystery",
        "rating": 4.5
    }
]


# Reading advice
def reading_advice(rating):

    if rating >= 4.5:
        return "Excellent book - Highly recommended for reading."

    elif rating >= 4.0:
        return "Very good book - Recommended for reading."

    elif rating >= 3.5:
        return "Good book - Worth reading."

    else:
        return "Average rating - You may try this book."


# Find and recommend books
def recommend_book(book_name):

    book_name = book_name.lower().strip()

    selected_book = None

    # Find the entered book
    for book in books:

        if book["title"].lower() == book_name:
            selected_book = book
            break

    # If book is not found
    if selected_book is None:

        print("\nBook not found.")
        print("Please enter a book from the available list.")

        return

    # Display selected book
    print("\n==========================================")
    print("              BOOK INFORMATION")
    print("==========================================")

    print("Title    :", selected_book["title"])
    print("Author   :", selected_book["author"])
    print("Category :", selected_book["category"])
    print("Rating   :", selected_book["rating"], "/ 5")

    print("Advice   :", reading_advice(
        selected_book["rating"]
    ))

    # Find recommendations
    recommendations = []

    for book in books:

        if book["title"] == selected_book["title"]:
            continue

        if book["category"] == selected_book["category"]:
            recommendations.append(book)

    # Display recommendations
    print("\n==========================================")
    print("           RECOMMENDED BOOKS")
    print("==========================================")

    if len(recommendations) == 0:

        print("No similar books found.")

    else:

        count = 0

        for book in recommendations:

            print("\n", count + 1, ".", book["title"])
            print("Author   :", book["author"])
            print("Category :", book["category"])
            print("Rating   :", book["rating"], "/ 5")
            print("Advice   :", reading_advice(
                book["rating"]
            ))

            count += 1

            if count == 5:
                break


# ==========================================================
#                     MAIN PROGRAM
# ==========================================================

print("=" * 55)
print("                    BOOK BUDDY")
print("              BOOK RECOMMENDATION SYSTEM")
print("=" * 55)

name = input("\nEnter your name: ")

print("\nWelcome,", name + "!")

print("\nAvailable books:")

for book in books:
    print("-", book["title"])

book_name = input("\nEnter a book name: ")

recommend_book(book_name)

print("\n==========================================")
print("Thank you for using Book Buddy!")
print("Happy Reading!")
print("==========================================")
