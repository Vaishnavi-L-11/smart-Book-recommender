# ==========================================================
#                     BOOK BUDDY
#       Smart Book Recommendation System
# ==========================================================

import urllib.request
import urllib.parse
import json


# ----------------------------------------------------------
# Search Books
# ----------------------------------------------------------

def search_book(book_name):

    query = urllib.parse.quote(book_name)

    url = (
        "https://openlibrary.org/search.json"
        "?q=" + query + "&limit=10"
    )

    try:

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "BookBuddyStudentProject/1.0"
            }
        )

        response = urllib.request.urlopen(
            request,
            timeout=10
        )

        data = json.loads(
            response.read().decode("utf-8")
        )

        return data.get("docs", [])

    except Exception:

        print("\nInternet connection problem.")
        return []


# ----------------------------------------------------------
# Create Rating
# ----------------------------------------------------------

def get_rating(book):

    rating = book.get("ratings_average")

    # If online rating exists
    if rating is not None:

        return round(rating, 1)

    # If rating is not available,
    # create a simple project rating
    popularity = book.get(
        "ratings_count",
        0
    )

    editions = book.get(
        "edition_count",
        0
    )

    score = 3.5

    if popularity > 100:
        score += 0.3

    if popularity > 1000:
        score += 0.3

    if popularity > 10000:
        score += 0.2

    if editions > 10:
        score += 0.1

    if score > 5:
        score = 5

    return round(score, 1)


# ----------------------------------------------------------
# Reading Advice
# ----------------------------------------------------------

def reading_advice(rating):

    if rating >= 4.5:

        return "Excellent rating - Highly recommended. You can read this!"

    elif rating >= 4.0:

        return "Very good rating - Recommended for reading."

    elif rating >= 3.5:

        return "Good rating - You can give this book a try."

    elif rating >= 3.0:

        return "Average rating - You may try this book."

    else:

        return "Low rating - Read reviews before choosing."


# ----------------------------------------------------------
# Display Book Information
# ----------------------------------------------------------

def show_book(book):

    title = book.get(
        "title",
        "Unknown"
    )

    authors = book.get(
        "author_name",
        ["Unknown"]
    )

    year = book.get(
        "first_publish_year",
        "Unknown"
    )

    rating = get_rating(book)

    print("\n==========================================")
    print("              BOOK INFORMATION")
    print("==========================================")

    print(
        "Title  :",
        title
    )

    print(
        "Author :",
        ", ".join(authors[:2])
    )

    print(
        "Year   :",
        year
    )

    print(
        "Rating :",
        rating,
        "/ 5"
    )

    print(
        "Advice :",
        reading_advice(rating)
    )


# ----------------------------------------------------------
# Recommend Similar Books
# ----------------------------------------------------------

def recommend_books(book):

    subjects = book.get(
        "subject",
        []
    )

    title = book.get(
        "title",
        ""
    )

    # If subjects are not available,
    # use the title for searching
    if subjects:

        search_text = " ".join(
            subjects[:3]
        )

    else:

        search_text = title


    results = search_book(
        search_text
    )

    print("\n==========================================")
    print("           BOOK RECOMMENDATIONS")
    print("==========================================")

    count = 0

    for item in results:

        item_title = item.get(
            "title",
            "Unknown"
        )

        if item_title.lower() == title.lower():
            continue

        authors = item.get(
            "author_name",
            ["Unknown"]
        )

        rating = get_rating(
            item
        )

        print(
            "\n",
            count + 1,
            ".",
            item_title
        )

        print(
            "Author :",
            ", ".join(authors[:2])
        )

        print(
            "Rating :",
            rating,
            "/ 5"
        )

        print(
            "Advice :",
            reading_advice(rating)
        )

        count += 1

        if count == 5:
            break

    if count == 0:

        print(
            "\nNo similar books were found."
        )


# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("=" * 55)

print("                    BOOK BUDDY")

print("       Smart Book Recommendation System")

print("=" * 55)


name = input(
    "\nEnter your name: "
).strip()


print(
    "\nWelcome,",
    name + "!"
)


# ==========================================================
# MAIN MENU
# ==========================================================

while True:

    print("\n==========================================")

    print("                 MAIN MENU")

    print("==========================================")

    print("1. Find a Book")
    print("2. Exit")

    print("==========================================")

    choice = input(
        "Enter your choice: "
    ).strip()


    # ------------------------------------------------------
    # Find Book
    # ------------------------------------------------------

    if choice == "1":

        book_name = input(
            "\nEnter any book name: "
        ).strip()

        print(
            "\nSearching for:",
            book_name
        )

        results = search_book(
            book_name
        )

        if not results:

            print(
                "\nBook could not be found."
            )

            continue


        selected_book = results[0]


        # Show information
        show_book(
            selected_book
        )


        # Recommend books
        recommend_books(
            selected_book
        )


    # ------------------------------------------------------
    # Exit
    # ------------------------------------------------------

    elif choice == "2":

        print(
            "\nThank you for using Book Buddy,"
            , name + "!"
        )

        print(
            "Happy Reading!"
        )

        break


    else:

        print(
            "\nPlease enter 1 or 2."
        )
